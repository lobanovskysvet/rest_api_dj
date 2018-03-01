from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from TaskApp.models import CustomUser
from TaskApp.utils import *
from .Serializers import UserAccountSerializer, UserViewSerializer, UserPasswordResetViewSerializer


@api_view(http_method_names=['POST'])
@parser_classes((JSONParser,))
def send_reset_password_link(request):
    if request.data['username'] and request.data['email']:
        userToResest = CustomUser.objects.filter(email=request.data['email'], username=request.data['username']).first()
        if userToResest is not None:
            send_reset_password_email(request.data['email'],
                                      get_encoded_base64_user_data_string(
                                          UserPasswordResetViewSerializer(request.data)))
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view()
def generate_new_password(request, pk):
    value = json.loads(get_decoded_base64_user_data_encoded_string(pk))
    userToResest = CustomUser.objects.filter(email=value['email'], username=value['username']).first()
    # Todo move to BL layer
    if userToResest is not None:
        newPassword = get_random_string()
        encodedPassword = make_password(newPassword)
        userToResest.password = encodedPassword
        serializer = UserViewSerializer(userToResest, data={"password": encodedPassword})
        if serializer.is_valid():
            serializer.save()
            # ToDo: send password via email instead of response
            return Response({"password": newPassword}, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(http_method_names=['POST'])
@parser_classes((JSONParser,))
@permission_classes((IsAuthenticated,))
def set_new_password(request, pk):
    if request.data['old_password'] and request.data['new_password']:
        userToUpdate = CustomUser.objects.filter(pk=pk).first()
        if userToUpdate is not None and userToUpdate.check_password(request.data['old_password']):
            newHashedPassword = make_password(request.data['new_password'])
            userToUpdate.password = newHashedPassword
            serializer = UserViewSerializer(userToUpdate, data={"password": newHashedPassword})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


class RegistrationView(APIView):

    def post(self, request):
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            generated_id = serializer.create(serializer.validated_data)
            return Response(generated_id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        customusers = CustomUser.objects.all()
        serializer = UserViewSerializer(customusers, many=True)
        return Response(serializer.data)


class UserViewDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(request, pk):
        return CustomUser.objects.get(pk=pk)

    def post(self, request, pk, format=None):
        customusers = self.get_object(pk)
        serializer = UserViewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        customusers = self.get_object(pk)
        serializer = UserViewSerializer(customusers)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        customusers = self.get_object(pk)
        serializer = UserViewSerializer(customusers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customusers = self.get_object(pk)
        customusers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

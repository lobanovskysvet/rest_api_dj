from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from TaskApp.models import CustomUser
from .Serializers import UserAccountSerializer, UserViewSerializer


class RegistrationView(APIView):
    def post(self, request):
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            generated_id = serializer.create(serializer.validated_data)
            return Response(generated_id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewList(APIView):
    def get(self, request, format=None):
        customusers = CustomUser.objects.all()
        serializer = UserViewSerializer(customusers, many=True)
        return Response(serializer.data)

class UserViewDetail(APIView):

    def get_object(request, pk):
        return CustomUser.objects.get(pk=pk)

    def post(self,request, pk, format=None):
        customusers = self.get_object(pk)
        serializer = UserViewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request, pk, format=None):
        customusers = self.get_object(pk)
        serializer = UserViewSerializer(customusers)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        customusers = self.get_object(pk)
        serializer = UserViewSerializer(customusers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk, format=None):
        customusers = self.get_object(pk)
        customusers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

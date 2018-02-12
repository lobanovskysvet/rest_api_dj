from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from TaskApp.models import CustomUser
from .Serializers import UserAccountSerializer, UserViewSerializer


class UserView(APIView):
    def get(self, request, format=None):
        serializer = UserViewSerializer(CustomUser.objects.all(), many=True)
        return Response(serializer.data)


class RegistrationView(APIView):
    def post(self, request):
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            generated_id = serializer.create(serializer.validated_data)
            return Response(generated_id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

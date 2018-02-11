from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .Serializers import UserSerializer


class TestView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)


class RegistrationView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

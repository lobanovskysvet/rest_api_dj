from rest_framework import serializers

from TaskApp.models import CustomUser
from django.contrib.auth.hashers import make_password
from .utils import send_email


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        send_email(validated_data['email'], 'Registration', 'Hi 123')
        user.password = make_password(validated_data['password'])
        user.save()
        return user.id


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'country')

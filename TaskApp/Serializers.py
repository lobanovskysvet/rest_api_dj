from rest_framework import serializers

from TaskApp.models import CustomUser
from django.contrib.auth.hashers import make_password


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def resto1re_object(self, attrs, instance=None):
        if instance is not None:
            instance.username = attrs.get('username ', instance.username)
            instance.password = attrs.get('password', instance.password)
            return instance
        return CustomUser(**attrs)

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.password = make_password(validated_data['password'])
        user.save()
        return user.id


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'country')

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if not user or not user.is_active:
            raise serializers.ValidationError("Invalid credentials")

        data['user'] = user
        return data


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["username", "password1", "password2", "first_name", "last_name", "email"]

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            error = serializers.ValidationError()
            error.status_code = 202
            raise error
        return value

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            error = serializers.ValidationError()
            error.status_code = 202
            raise error
        return value

    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError("Passwords do not match.")

        return data

    def create(self, validated_data):
        password1 = validated_data.pop('password1')
        validated_data.pop('password2')

        user = CustomUser.objects.create_user(password=password1, **validated_data)
        return user

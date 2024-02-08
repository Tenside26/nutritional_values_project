from rest_framework import serializers
from users_app.models import CustomUser
from calculator_app.models import Product


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "pk", "username", "first_name", "last_name", "email"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

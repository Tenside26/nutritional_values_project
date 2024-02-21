from rest_framework import serializers
from users_app.models import CustomUser
from calculator_app.models import Product, Meal


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("pk", "username", "first_name", "last_name", "email")


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("pk", "name", "serving_size", "calories", "protein", "carbohydrate", "fat")


class MealSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    product = ProductSerializer(many=True)

    class Meta:
        model = Meal
        fields = ("pk", "user", "product")

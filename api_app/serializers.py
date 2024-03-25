from rest_framework import serializers
from users_app.models import CustomUser
from calculator_app.models import Product, Meal, UserModifiedProduct


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("pk",
                  "username",
                  "first_name",
                  "last_name",
                  "email")


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("pk",
                  "name",
                  "serving_size",
                  "calories",
                  "protein",
                  "carbohydrate",
                  "fat")


class MealSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Meal
        fields = ("pk",
                  "user",
                  "title",
                  "date_created",
                  "date_updated",
                  "total_calories",
                  "total_protein",
                  "total_carbohydrate",
                  "total_fat")


class UserModifiedProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    meal = MealSerializer()

    class Meta:
        model = UserModifiedProduct
        fields = ("pk",
                  "name",
                  "product",
                  "meal",
                  "serving_size",
                  "calories",
                  "protein",
                  "carbohydrate",
                  "fat")

from rest_framework import serializers
from users_app.models import CustomUser
from calculator_app.models import Product, Meal, UserModifiedProduct
from rest_framework.exceptions import ValidationError


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
    product_id = serializers.IntegerField(write_only=True)
    meal_pk = serializers.IntegerField(write_only=True)

    class Meta:
        model = UserModifiedProduct
        fields = ("pk",
                  "name",
                  "product_id",
                  "meal_pk",
                  "serving_size",
                  "calories",
                  "protein",
                  "carbohydrate",
                  "fat")

    def validate(self, data):
        product_id = data.get('product_id')
        serving_size = data.get('serving_size')
        meal_pk = data.get('meal_pk')

        if not meal_pk or not product_id or not serving_size:
            raise ValidationError({"message": "Missing required fields."})

        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError({"message": "The specified product does not exist."})

        try:
            Meal.objects.get(pk=meal_pk)
        except Meal.DoesNotExist:
            raise ValidationError({"message": "The specified meal does not exist."})

        if serving_size <= 0:
            raise ValidationError({"message": "Serving size must be a positive number."})

        return data

    def create(self, validated_data):
        product_id = validated_data.pop('product_id')
        meal_pk = validated_data.pop('meal_pk')

        product = Product.objects.get(id=product_id)
        meal = Meal.objects.get(pk=meal_pk)

        instance = UserModifiedProduct.objects.create(product=product, meal=meal, **validated_data)
        return instance

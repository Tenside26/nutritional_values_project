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


class UserModifiedProductSerializerCreate(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)
    meal_id = serializers.PrimaryKeyRelatedField(queryset=Meal.objects.all(), write_only=True)

    class Meta:
        model = UserModifiedProduct
        fields = ("pk",
                  "name",
                  "product_id",
                  "meal_id",
                  "serving_size",
                  "calories",
                  "protein",
                  "carbohydrate",
                  "fat")

    def validate_serving_size(self, serving_size):
        if serving_size <= 0:
            raise serializers.ValidationError({"message": "Serving size must be a positive number."})

        elif not serving_size:
            raise serializers.ValidationError({"message": "Serving size field must be filled."})

        return serving_size

    def validate(self, data):
        self.validate_serving_size(data.get('serving_size'))

        return data

    def create(self, validated_data):
        product = validated_data.pop('product_id')
        meal = validated_data.pop('meal_id')

        instance = UserModifiedProduct.objects.create(product=product, meal=meal, **validated_data)
        return instance


class UserModifiedProductSerializerUpdate(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)
    meal_id = serializers.PrimaryKeyRelatedField(queryset=Meal.objects.all(), write_only=True)

    class Meta:
        model = UserModifiedProduct
        fields = ("pk",
                  "name",
                  "product_id",
                  "meal_id",
                  "serving_size",
                  "calories",
                  "protein",
                  "carbohydrate",
                  "fat")

    def validate_serving_size(self, serving_size):
        if serving_size <= 0:
            raise serializers.ValidationError({"message": "Serving size must be a positive number."})

        elif not serving_size:
            raise serializers.ValidationError({"message": "Serving size field must be filled."})

        return serving_size

    def validate(self, data):
        self.validate_serving_size(data.get('serving_size'))

        return data

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.product_id = validated_data.get('product_id', instance.product_id)
        instance.meal_id = validated_data.get('meal_id', instance.meal_id)
        instance.serving_size = validated_data.get('serving_size', instance.serving_size)
        instance.calories = validated_data.get('calories', instance.calories)
        instance.protein = validated_data.get('protein', instance.protein)
        instance.carbohydrate = validated_data.get('carbohydrate', instance.carbohydrate)
        instance.fat = validated_data.get('fat', instance.fat)
        instance.save()
        return instance


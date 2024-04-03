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

    def validate_product_exists(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError({"message": "The specified product does not exist."})

        return product_id

    def validate_meal_exists(self, meal_pk):
        try:
            Meal.objects.get(pk=meal_pk)
        except Meal.DoesNotExist:
            raise serializers.ValidationError({"message": "The specified meal does not exist."})

        return meal_pk

    def validate_serving_size(self, serving_size):
        if serving_size <= 0:
            raise serializers.ValidationError({"message": "Serving size must be a positive number."})

        return serving_size

    def validate(self, data):
        self.validate_product_exists(data.get('product_id'))
        self.validate_meal_exists(data.get('meal_pk'))
        self.validate_serving_size(data.get('serving_size'))

        return data

    def create(self, validated_data):
        product_id = validated_data.pop('product_id')
        meal_pk = validated_data.pop('meal_pk')

        product = Product.objects.get(id=product_id)
        meal = Meal.objects.get(pk=meal_pk)

        instance = UserModifiedProduct.objects.create(product=product, meal=meal, **validated_data)
        return instance


class UserModifiedProductSerializerUpdate(serializers.ModelSerializer):
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

    def validate_modified_product_db_product_exists(self):
        existing_product = self.instance

        if existing_product and not existing_product.product_id:
            raise serializers.ValidationError({"message": "modified_product does not have product_id set."})

        elif not existing_product:
            raise serializers.ValidationError({"message": "modified_product does not exist."})

        return existing_product.product_id

    def validate_modified_product_meal_exists(self):
        existing_product = self.instance

        if existing_product and not existing_product.meal_id:
            raise serializers.ValidationError({"message": "modified_product does not have meal_pk set."})

        elif not existing_product:
            raise serializers.ValidationError({"message": "modified_product does not exist."})

        return existing_product.meal_id

    def validate_serving_size(self, serving_size):
        if serving_size <= 0:
            raise serializers.ValidationError({"message": "Serving size must be a positive number."})

        return serving_size

    def validate(self, data):
        self.validate_serving_size(data.get('serving_size'))
        self.validate_modified_product_db_product_exists()
        self.validate_modified_product_meal_exists()

        return data

    def update(self, instance, validated_data):

        if instance.product_id and instance.meal_id:
            instance.product = Product.objects.get(id=instance.product_id)
            instance.meal = Meal.objects.get(pk=instance.meal_id)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


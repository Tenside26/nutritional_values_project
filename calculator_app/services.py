from django.db.models import Sum
from api_app.serializers import UserModifiedProductSerializer
from .models import Meal, UserModifiedProduct
from rest_framework.response import Response
from rest_framework import status


def calculate_nutritional_values_per_serving_size(instance):
    modified_serving_size = instance.serving_size / instance.product.serving_size
    instance.name = instance.product.name
    instance.calories = instance.product.calories * modified_serving_size
    instance.protein = instance.product.protein * modified_serving_size
    instance.carbohydrate = instance.product.carbohydrate * modified_serving_size
    instance.fat = instance.product.fat * modified_serving_size
    instance.save()


def sum_meal_nutritional_values(meal_id):
    meal = Meal.objects.get(id=meal_id)
    aggregated_values = meal.modified_product.all().aggregate(
        total_calories=Sum('calories'),
        total_protein=Sum('protein'),
        total_carbohydrate=Sum('carbohydrate'),
        total_fat=Sum('fat')
    )

    meal.total_calories = aggregated_values['total_calories']
    meal.total_protein = aggregated_values['total_protein']
    meal.total_carbohydrate = aggregated_values['total_carbohydrate']
    meal.total_fat = aggregated_values['total_fat']
    meal.save()


def create_user_modified_product(request_data, meal_id):
    request_data["meal_pk"] = meal_id
    serializer = UserModifiedProductSerializer(data=request_data)

    if serializer.is_valid():
        serializer.save()
        calculate_nutritional_values_per_serving_size(serializer.instance)
        sum_meal_nutritional_values(meal_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        errors = serializer.errors
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


def partial_update_user_modified_product(request_data, meal_id, modified_product_id):
    existing_product = UserModifiedProduct.objects.get(id=modified_product_id)
    serializer = UserModifiedProductSerializer(data=request_data, instance=existing_product, partial=True)

    if serializer.is_valid():
        serializer.save()
        calculate_nutritional_values_per_serving_size(serializer.instance)
        sum_meal_nutritional_values(meal_id)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    else:
        errors = serializer.errors
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

from django.db.models import Sum


def calculate_nutritional_values_per_serving_size(instance):
    modified_serving_size = instance.serving_size / instance.product.serving_size
    instance.name = instance.product.name
    instance.calories = instance.product.calories * modified_serving_size
    instance.protein = instance.product.protein * modified_serving_size
    instance.carbohydrate = instance.product.carbohydrate * modified_serving_size
    instance.fat = instance.product.fat * modified_serving_size


def sum_meal_nutritional_values(instance):
    aggregated_values = instance.modified_product.all().aggregate(
        total_calories=Sum('calories'),
        total_protein=Sum('protein'),
        total_carbohydrate=Sum('carbohydrate'),
        total_fat=Sum('fat')
    )

    instance.total_calories = aggregated_values['total_calories']
    instance.total_protein = aggregated_values['total_protein']
    instance.total_carbohydrate = aggregated_values['total_carbohydrate']
    instance.total_fat = aggregated_values['total_fat']

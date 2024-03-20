

def calculate_totals(instance):
    modified_serving_size = instance.serving_size / instance.product.serving_size
    instance.name = instance.product.name
    instance.calories = instance.product.calories * modified_serving_size
    instance.protein = instance.product.protein * modified_serving_size
    instance.carbohydrate = instance.product.carbohydrate * modified_serving_size
    instance.fat = instance.product.fat * modified_serving_size

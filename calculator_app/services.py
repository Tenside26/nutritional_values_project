

def calculate_totals(modified_product, database_product):
    modified_serving_size = modified_product.serving_size / database_product.product.serving_size
    modified_product.name = database_product.product.name
    modified_product.calories = database_product.product.calories * modified_serving_size
    modified_product.protein = database_product.product.protein * modified_serving_size
    modified_product.carbohydrate = database_product.product.carbohydrate * modified_serving_size
    modified_product.fat = database_product.product.fat * modified_serving_size

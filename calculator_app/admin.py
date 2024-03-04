from django.contrib import admin
from .models import Product, Meal


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ["name", "serving_size", "calories", "protein", "carbohydrate", "fat",]


@admin.register(Meal)
class AdminMeal(admin.ModelAdmin):
    list_display = ["user", "date"]

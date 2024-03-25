from django.contrib import admin
from .models import Product, Meal, UserModifiedProduct


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ["name", "serving_size", "calories", "protein", "carbohydrate", "fat",]


@admin.register(UserModifiedProduct)
class AdminUserModifiedProduct(admin.ModelAdmin):
    list_display = ["name", "product", "meal", "serving_size", "calories", "protein", "carbohydrate", "fat",]


@admin.register(Meal)
class AdminMeal(admin.ModelAdmin):
    list_display = ["title", "user", "date_created", "date_updated"]

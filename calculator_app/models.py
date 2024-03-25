from django.db import models
from users_app.models import CustomUser
from .validators import name_validator


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False, validators=[name_validator])
    serving_size = models.IntegerField(default=100)
    calories = models.IntegerField()
    protein = models.FloatField()
    carbohydrate = models.FloatField()
    fat = models.FloatField()


class Meal(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_meal")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    total_calories = models.IntegerField(default=0)
    total_protein = models.FloatField(default=0.0)
    total_carbohydrate = models.FloatField(default=0.0)
    total_fat = models.FloatField(default=0.0)


class UserModifiedProduct(models.Model):
    name = models.CharField(default="string", blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="related_product")
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="modified_product")
    serving_size = models.IntegerField(default=100)
    calories = models.IntegerField(default=0, blank=True)
    protein = models.FloatField(default=0.0, blank=True)
    carbohydrate = models.FloatField(default=0.0, blank=True)
    fat = models.FloatField(default=0.0, blank=True)

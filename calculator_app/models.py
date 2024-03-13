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


class UserModifiedProduct(models.Model):
    name = models.CharField(default="string")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="related_product")
    serving_size = models.IntegerField(default=100)
    calories = models.IntegerField(default=0)
    protein = models.FloatField(default=0.0)
    carbohydrate = models.FloatField(default=0.0)
    fat = models.FloatField(default=0.0)


class Meal(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="meal_user")
    product = models.ManyToManyField(UserModifiedProduct)
    date = models.DateTimeField(auto_now_add=True)

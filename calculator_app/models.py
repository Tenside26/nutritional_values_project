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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="meal_user")
    product = models.ManyToManyField(Product)
    date = models.DateTimeField(auto_now_add=True)

from django.db import models
from users_app.models import CustomUser


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    serving_size = models.IntegerField(default=100, blank=False, null=False)
    calories = models.IntegerField()
    protein = models.DecimalField(max_digits=15, decimal_places=2)
    carbohydrate = models.DecimalField(max_digits=15, decimal_places=2)
    fat = models.DecimalField(max_digits=15, decimal_places=2)


class Meal(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="meal_user")
    product = models.ManyToManyField(Product)

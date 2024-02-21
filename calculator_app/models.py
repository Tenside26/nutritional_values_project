from django.db import models
from users_app.models import CustomUser
from django.core.validators import RegexValidator


class Product(models.Model):
    name_validator = RegexValidator(
        regex='^[a-zA-Z,]+$',
        message='Enter only alphabetical characters with or without commas.',
        code='invalid_name'
    )

    name = models.CharField(max_length=255, unique=True, blank=False, null=False, validators=[name_validator])
    serving_size = models.IntegerField(default=100)
    calories = models.IntegerField()
    protein = models.FloatField()
    carbohydrate = models.FloatField()
    fat = models.FloatField()


class Meal(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="meal_user")
    product = models.ManyToManyField(Product)

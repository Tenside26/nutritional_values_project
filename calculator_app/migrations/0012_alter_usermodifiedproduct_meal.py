# Generated by Django 5.0.1 on 2024-03-20 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator_app', '0011_remove_meal_products_usermodifiedproduct_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodifiedproduct',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_meal', to='calculator_app.meal'),
        ),
    ]

# Generated by Django 5.0.1 on 2024-03-18 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator_app', '0008_rename_date_meal_date_created_meal_date_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_modified_product', to='calculator_app.usermodifiedproduct'),
        ),
    ]

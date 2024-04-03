# Generated by Django 5.0.1 on 2024-03-13 16:12

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator_app', '0006_meal_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModifiedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Enter only alphabetical characters with or without commas.', regex='^[a-zA-Z,]+$')])),
                ('serving_size', models.IntegerField(default=100)),
                ('calories', models.IntegerField()),
                ('protein', models.FloatField()),
                ('carbohydrate', models.FloatField()),
                ('fat', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_product', to='calculator_app.product')),
            ],
        ),
        migrations.AlterField(
            model_name='meal',
            name='product',
            field=models.ManyToManyField(to='calculator_app.usermodifiedproduct'),
        ),
    ]

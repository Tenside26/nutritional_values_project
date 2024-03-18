from rest_framework import serializers
from calculator_app.models import UserModifiedProduct


class UserModifiedProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModifiedProduct
        fields = ("pk",
                  "name",
                  "serving_size",
                  "calories",
                  "protein",
                  "carbohydrate",
                  "fat")
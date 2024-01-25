from rest_framework import serializers
from users_app.models import CustomUser


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "username", "first_name", "last_name", "email"

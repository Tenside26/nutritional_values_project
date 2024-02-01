
from rest_framework import generics
from users_app.models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer





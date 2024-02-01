from calculator_app.models import Product
from rest_framework import generics
from users_app.models import CustomUser
from .serializers import CustomUserSerializer, ProductSerializer


class CustomUserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer





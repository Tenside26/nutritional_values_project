from calculator_app.models import Product
from users_app.models import CustomUser
from .serializers import CustomUserSerializer, ProductSerializer
from rest_framework.viewsets import ModelViewSet


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

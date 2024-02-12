from calculator_app.models import Product
from users_app.models import CustomUser
from .serializers import CustomUserSerializer, ProductSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet


class ProductPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class CustomUserPageNumberPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def list(self, request, *args, **kwargs):
        self.pagination_class = CustomUserPageNumberPagination
        return super().list(request, *args, **kwargs)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        self.pagination_class = ProductPageNumberPagination
        return super().list(request, *args, **kwargs)

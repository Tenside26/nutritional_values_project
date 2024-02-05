from calculator_app.models import Product
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, ListAPIView
from users_app.models import CustomUser
from .serializers import CustomUserSerializer, ProductSerializer
from rest_framework.pagination import PageNumberPagination


class ProductPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class CustomUserPageNumberPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'


class CustomUserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    pagination_class = CustomUserPageNumberPagination


class CustomUserDetailView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserUpdateView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDestroyView(DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPageNumberPagination


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDestroyView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

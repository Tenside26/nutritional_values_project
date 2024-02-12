
from django.urls import path
from .views import (CustomUserViewSet, ProductViewSet)


urlpatterns = [
    path('users-list/', CustomUserViewSet.as_view({'get': 'list'}), name='api-users-list'),
    path('user/<int:pk>/', CustomUserViewSet.as_view({'get': 'retrieve'}), name='api-user-detail'),
    path('user/create', CustomUserViewSet.as_view({'post': 'create'}), name='api-user-create'),
    path('user/update/<int:pk>/', CustomUserViewSet.as_view({'put': 'update'}), name='api-user-update'),
    path('user/destroy/<int:pk>/', CustomUserViewSet.as_view({'delete': 'destroy'}), name='api-user-destroy'),
    path('products-list/', ProductViewSet.as_view({'get': 'list'}), name='api-products-list'),
    path('product/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'}), name='api-product-detail'),
    path('product/create', ProductViewSet.as_view({'post': 'create'}), name='api-product-create'),
    path('product/update/<int:pk>/', ProductViewSet.as_view({'put': 'update'}), name='api-product-update'),
    path('product/destroy/<int:pk>/', ProductViewSet.as_view({'delete': 'destroy'}), name='api-product-destroy'),
]
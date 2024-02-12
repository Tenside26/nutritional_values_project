
from django.urls import path
from .views import (CustomUserViewSet, ProductListView, ProductDetailView, ProductUpdateView,
                    ProductDestroyView, ProductCreateView)


urlpatterns = [
    path('users-list/', CustomUserViewSet.as_view({'get': 'list'}), name='api-users-list'),
    path('user/<int:pk>/', CustomUserViewSet.as_view({'get': 'retrieve'}), name='api-user-detail'),
    path('user/create', CustomUserViewSet.as_view({'post': 'create'}), name='api-user-create'),
    path('user/update/<int:pk>/', CustomUserViewSet.as_view({'put': 'update'}), name='api-user-update'),
    path('user/destroy/<int:pk>/', CustomUserViewSet.as_view({'delete': 'destroy'}), name='api-user-destroy'),
    path('products-list/', ProductListView.as_view(), name='api-products-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='api-product-detail'),
    path('product/create', ProductCreateView.as_view(), name='api-product-create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='api-product-update'),
    path('product/destroy/<int:pk>/', ProductDestroyView.as_view(), name='api-product-destroy'),
]
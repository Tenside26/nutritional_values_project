
from django.urls import path
from .views import (CustomUserListView, ProductListView, ProductDetailView, ProductUpdateView,
                    ProductDestroyView, ProductCreateView, CustomUserCreateView, CustomUserDetailView,
                    CustomUserDestroyView, CustomUserUpdateView)


urlpatterns = [
    path('users-list/', CustomUserListView.as_view(), name='api-users-list'),
    path('user/<int:pk>/', CustomUserDetailView.as_view(), name='api-user-detail'),
    path('user/create', CustomUserCreateView.as_view(), name='api-user-create'),
    path('user/update/<int:pk>/', CustomUserUpdateView.as_view(), name='api-user-update'),
    path('user/destroy/<int:pk>/', CustomUserDestroyView.as_view(), name='api-user-destroy'),
    path('products-list/', ProductListView.as_view(), name='api-products-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='api-product-detail'),
    path('product/create', ProductCreateView.as_view(), name='api-product-create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='api-product-update'),
    path('product/destroy/<int:pk>/', ProductDestroyView.as_view(), name='api-product-destroy'),
]
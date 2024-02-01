
from django.urls import path
from .views import CustomUserListView, ProductListView, ProductDetailView, ProductUpdateView

urlpatterns = [
    path('users-list/', CustomUserListView.as_view(), name='api-users-list'),
    path('products-list/', ProductListView.as_view(), name='api-products-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='api-product-detail'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='api-product-update'),
]
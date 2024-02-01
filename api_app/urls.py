
from django.urls import path
from .views import CustomUserListView, ProductListView

urlpatterns = [
    path('users-list/', CustomUserListView.as_view(), name='api-users-list'),
    path('products-list/', ProductListView.as_view(), name='api-products-list'),
]
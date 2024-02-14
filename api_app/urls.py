
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'users', CustomUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
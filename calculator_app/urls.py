from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MealUserViewSet, ModifiedProductViewSet

router = DefaultRouter()
router.register(r'user-meals', MealUserViewSet, basename='user-meals'),
router.register(r'modified-product', ModifiedProductViewSet, basename='modified-product')

urlpatterns = [
    path('', include(router.urls)),
]
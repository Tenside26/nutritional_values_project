from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MealUserViewSet

router = DefaultRouter()
router.register(r'user-meals', MealUserViewSet, basename='user-meals')

urlpatterns = [
    path('', include(router.urls)),
]
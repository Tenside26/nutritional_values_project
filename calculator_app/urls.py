from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MealUserViewSet, ModifiedProductViewSet

router = DefaultRouter()
router.register(r'user-meals', MealUserViewSet, basename='user-meals'),
router.register(r'modified-product', ModifiedProductViewSet, basename='modified-product')

urlpatterns = [
    path('', include(router.urls)),

    path('user-meals/<int:meal_pk>/modified-product/',
         ModifiedProductViewSet.as_view({
             'post': 'create',
         }), name='modified-product-list'),

    path('user-meals/<int:meal_pk>/modified-product/<int:pk>/',
         ModifiedProductViewSet.as_view({
             'patch': 'partial_update',
             'delete': 'destroy',
         }), name='modified-product-detail'),
]

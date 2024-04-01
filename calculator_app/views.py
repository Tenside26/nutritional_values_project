
from rest_framework.viewsets import ModelViewSet
from calculator_app.models import Meal, UserModifiedProduct
from api_app.serializers import MealSerializer, UserModifiedProductSerializer
from django_filters import rest_framework
from .services import create_user_modified_product, partial_update_user_modified_product, sum_meal_nutritional_values
from rest_framework.response import Response
from rest_framework import status


class MealUserFilter(rest_framework.FilterSet):
    date_created_gte = rest_framework.DateFilter(field_name='date_created', lookup_expr='gte')
    date_created_lte = rest_framework.DateFilter(field_name='date_created', lookup_expr='lte')
    title = rest_framework.CharFilter(field_name='title', lookup_expr='icontains')
    product_name = rest_framework.CharFilter(field_name='product__name', lookup_expr='icontains')

    class Meta:
        model = Meal
        fields = ['title', 'date_created_gte', 'date_created_lte', 'product_name']


class MealUserViewSet(ModelViewSet):
    serializer_class = MealSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = MealUserFilter

    def get_queryset(self):
        queryset = Meal.objects.filter(user=self.request.user)

        return queryset


class ModifiedProductViewSet(ModelViewSet):
    serializer_class = UserModifiedProductSerializer

    def create(self, request, *args, **kwargs):
        response = create_user_modified_product(request.data, kwargs.get('meal_pk'))

        if isinstance(response, Response):
            return response
        else:
            return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, *args, **kwargs):
        response = partial_update_user_modified_product(request.data, kwargs.get('meal_pk'), kwargs.get('pk'))

        if isinstance(response, Response):
            return response
        else:
            return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        meal_pk = kwargs.get('meal_pk')
        pk = kwargs.get('pk')

        try:
            modified_product = UserModifiedProduct.objects.get(meal__pk=meal_pk, pk=pk)
        except UserModifiedProduct.DoesNotExist:
            return Response({"message": "Product not found for the specified meal."},
                            status=status.HTTP_404_NOT_FOUND)

        modified_product.delete()
        sum_meal_nutritional_values(meal_pk)

        return Response({"message": "Product deleted successfully."},
                        status=status.HTTP_204_NO_CONTENT)


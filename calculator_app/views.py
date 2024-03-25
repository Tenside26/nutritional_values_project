
from rest_framework.viewsets import ModelViewSet
from calculator_app.models import Meal, UserModifiedProduct, Product
from api_app.serializers import MealSerializer, UserModifiedProductSerializer
from django_filters import rest_framework
from rest_framework.response import Response
from rest_framework import status
from .services import calculate_nutritional_values_per_serving_size, sum_meal_nutritional_values


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
        product_id = request.data.get('product')
        serving_size = request.data.get('serving_size')
        meal_pk = kwargs.get('meal_pk')

        if not meal_pk or not product_id or not serving_size:
            return Response({"message": "Missing required fields."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"message": "The specified product does not exist."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            meal = Meal.objects.get(pk=meal_pk)
        except Meal.DoesNotExist:
            return Response({"message": "The specified meal does not exist."},
                            status=status.HTTP_400_BAD_REQUEST)

        if serving_size <= 0:
            return Response({"message": "Serving size must be a positive number."},
                            status=status.HTTP_400_BAD_REQUEST)

        user_modified_product = UserModifiedProduct(product=product, meal=meal, serving_size=serving_size)
        calculate_nutritional_values_per_serving_size(user_modified_product)
        user_modified_product.save()
        sum_meal_nutritional_values(meal)
        meal.save()

        serializer = self.get_serializer(user_modified_product)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

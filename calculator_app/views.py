
from rest_framework.viewsets import ModelViewSet
from calculator_app.models import Meal
from api_app.serializers import MealSerializer
from django_filters import rest_framework


class MealUserFilter(rest_framework.FilterSet):
    date_gte = rest_framework.DateFilter(field_name='date', lookup_expr='gte')
    date_lte = rest_framework.DateFilter(field_name='date', lookup_expr='lte')
    product_name = rest_framework.CharFilter(field_name='product__name', lookup_expr='icontains')

    class Meta:
        model = Meal
        fields = ['date_gte', 'date_lte', 'product_name']


class MealUserViewSet(ModelViewSet):
    serializer_class = MealSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = MealUserFilter

    def get_queryset(self):
        queryset = Meal.objects.filter(user=self.request.user)

        return queryset

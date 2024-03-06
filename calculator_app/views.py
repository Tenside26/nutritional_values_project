
from rest_framework.viewsets import ModelViewSet
from calculator_app.models import Meal
from api_app.serializers import MealSerializer
from django_filters import rest_framework


class MealUserFilter(rest_framework.FilterSet):
    date = rest_framework.DateFilter(field_name='date', lookup_expr='date')

    class Meta:
        model = Meal
        fields = ['date']


class MealUserViewSet(ModelViewSet):
    serializer_class = MealSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = MealUserFilter

    def get_queryset(self):
        queryset = Meal.objects.filter(user=self.request.user)

        return queryset

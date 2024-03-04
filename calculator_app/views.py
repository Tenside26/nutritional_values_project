from rest_framework import filters
from rest_framework.generics import ListAPIView
from datetime import datetime
from calculator_app.models import Meal
from api_app.serializers import MealSerializer


class MealUserView(ListAPIView):
    serializer_class = MealSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['selected_date']

    def get_queryset(self):
        selected_date = self.request.query_params.get('selected_date', None)
        queryset = Meal.objects.filter(user=self.request.user)

        if selected_date:
            selected_datetime = datetime.strptime(selected_date, "%Y-%m-%d").date()
            queryset = queryset.filter(date=selected_datetime)

        return queryset

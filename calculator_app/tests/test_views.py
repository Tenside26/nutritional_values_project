from rest_framework.authtoken.models import Token
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from faker import Faker
from calculator_app.models import Meal
from api_app.serializers import MealSerializer
from users_app.factories import CustomUserFactory
from calculator_app.factories import ProductFactory, MealFactory


class MealUserViewsTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.fake = Faker()

        self.product = ProductFactory()
        self.user = CustomUserFactory()
        self.meal = MealFactory(user=self.user)
        self.meal.product.set([self.product])
        self.token = Token.objects.create(user=self.user)

        self.list_url = reverse('user-meals-list')
        self.detail_url = reverse('user-meals-detail', args=[self.meal.pk])
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_api_view_meal_user_list_get(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_meals = Meal.objects.filter(user=self.user)
        serialized_data = MealSerializer(expected_meals, many=True).data

        self.assertEqual(response.data['count'], len(expected_meals))
        self.assertEqual(response.data['next'], None)
        self.assertEqual(response.data['previous'], None)
        self.assertEqual(response.data['results'], serialized_data)


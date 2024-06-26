from rest_framework.authtoken.models import Token
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from users_app.models import CustomUser
from calculator_app.models import Product, Meal
from faker import Faker
from api_app.serializers import CustomUserSerializer, ProductSerializer, MealSerializer
from users_app.factories import CustomUserFactory
from calculator_app.factories import ProductFactory, MealFactory


class CustomUserViewsTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.fake = Faker()

        self.user = CustomUserFactory()
        self.token = Token.objects.create(user=self.user)
        self.input_user_data = {
            'username': self.fake.user_name(),
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'email': self.fake.email(),
        }

        self.list_url = reverse('user-list')
        self.detail_url = reverse('user-detail', args=[self.user.pk])
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_user_list_api_view_get(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_users = CustomUser.objects.all()
        serialized_data = CustomUserSerializer(expected_users, many=True).data
        self.assertEqual(response.data['count'], len(expected_users))
        self.assertEqual(response.data['next'], None)
        self.assertEqual(response.data['previous'], None)
        self.assertEqual(response.data['results'], serialized_data)

    def test_user_detail_api_view_get(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_users = CustomUser.objects.get(pk=self.user.pk)
        serialized_data = CustomUserSerializer(expected_users).data
        self.assertEqual(response.data, serialized_data)

    def test_user_create_api_view_post(self):
        response = self.client.post(self.list_url, self.input_user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        expected_user = CustomUser.objects.get(pk=response.data['pk'])
        serialized_data = CustomUserSerializer(expected_user).data
        self.assertEqual(response.data, serialized_data)

    def test_user_update_api_view_put_patch(self):
        updated_data = {
            'username': self.input_user_data["username"],
            'email': self.input_user_data["email"],
        }

        response = self.client.patch(self.detail_url, data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_user = CustomUser.objects.get(pk=self.user.pk)
        serialized_data = CustomUserSerializer(updated_user).data
        self.assertEqual(response.data, serialized_data)
        self.assertEqual(updated_user.username, self.input_user_data["username"])
        self.assertEqual(updated_user.email, self.input_user_data["email"])

    def test_user_destroy_api_view_delete(self):
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ProductViewsTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.fake = Faker()
        self.user = CustomUserFactory()
        self.token = Token.objects.create(user=self.user)

        self.product = ProductFactory()
        self.input_product_data = {
            'name': self.fake.word(),
            'serving_size': self.fake.random_int(min=1, max=2000),
            'calories': self.fake.random_int(min=1, max=2000),
            'protein': self.fake.pyfloat(left_digits=2, right_digits=2, positive=True),
            'carbohydrate': self.fake.pyfloat(left_digits=2, right_digits=2, positive=True),
            'fat': self.fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        }

        self.detail_url = reverse('product-detail', args=[self.product.pk])
        self.list_url = reverse('product-list')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_api_view_product_list_get(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_product = Product.objects.all()
        serialized_data = ProductSerializer(expected_product, many=True).data
        self.assertEqual(response.data['count'], len(expected_product))
        self.assertEqual(response.data['next'], None)
        self.assertEqual(response.data['previous'], None)
        self.assertEqual(response.data['results'], serialized_data)

    def test_api_view_product_detail_get(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_product = Product.objects.get(pk=self.product.pk)
        serialized_data = ProductSerializer(expected_product).data
        self.assertEqual(response.data, serialized_data)

    def test_api_view_product_create_post(self):
        response = self.client.post(self.list_url, self.input_product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        expected_product = Product.objects.get(pk=response.data['pk'])
        serialized_data = ProductSerializer(expected_product).data
        self.assertEqual(response.data, serialized_data)

    def test_api_view_product_update_put_patch(self):
        updated_data = {
            'name': self.input_product_data["name"],
            'serving_size': self.input_product_data["serving_size"],
        }

        response = self.client.patch(self.detail_url, data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_product = Product.objects.get(pk=self.product.pk)
        serialized_data = ProductSerializer(updated_product).data
        self.assertEqual(response.data, serialized_data)
        self.assertEqual(updated_product.name, self.input_product_data["name"])
        self.assertEqual(updated_product.serving_size, self.input_product_data["serving_size"])

    def test_api_view_product_delete(self):
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class MealViewsTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.fake = Faker()

        self.user = CustomUserFactory()
        self.token = Token.objects.create(user=self.user)
        self.meal = MealFactory(user=self.user)

        self.detail_url = reverse('meal-detail', args=[self.meal.pk])
        self.list_url = reverse('meal-list')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_api_view_meal_list_get(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_meal = Meal.objects.all()
        serialized_data = MealSerializer(expected_meal, many=True).data
        self.assertEqual(response.data['count'], len(expected_meal))
        self.assertEqual(response.data['next'], None)
        self.assertEqual(response.data['previous'], None)
        self.assertEqual(response.data['results'], serialized_data)

    def test_api_view_meal_detail_get(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_meal = Meal.objects.get(pk=self.meal.pk)
        serialized_data = MealSerializer(expected_meal).data
        self.assertEqual(response.data, serialized_data)

    def test_api_view_meal_create_post(self):
        pass

    def test_api_view_meal_update_put_patch(self):
        pass

    def test_api_view_meal_delete(self):
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

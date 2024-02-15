
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from users_app.models import CustomUser
from calculator_app.models import Product
from faker import Faker
from api_app.serializers import CustomUserSerializer, ProductSerializer
from users_app.factories import CustomUserFactory
from calculator_app.factories import ProductFactory


class CustomUserViewsTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.fake = Faker()

        self.user = CustomUserFactory()
        self.test_user_data = {
            'username': self.fake.user_name(),
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'email': self.fake.email(),
        }

    def test_user_list_api_view_get(self):
        list_url = reverse('user-list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_users = CustomUser.objects.all()
        serialized_data = CustomUserSerializer(expected_users, many=True).data
        self.assertEqual(response.data['count'], len(expected_users))
        self.assertEqual(response.data['next'], None)
        self.assertEqual(response.data['previous'], None)
        self.assertEqual(response.data['results'], serialized_data)

    def test_user_detail_api_view_get(self):
        detail_url = reverse('user-detail', args=[self.user.pk])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_users = CustomUser.objects.get(pk=self.user.pk)
        serialized_data = CustomUserSerializer(expected_users).data
        self.assertEqual(response.data, serialized_data)

    def test_user_create_api_view_post(self):
        create_url = reverse('user-list')
        response = self.client.post(create_url, self.test_user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        expected_user = CustomUser.objects.get(pk=response.data['pk'])
        serialized_data = CustomUserSerializer(expected_user).data
        self.assertEqual(response.data, serialized_data)

    def test_user_update_api_view_put_patch(self):
        detail_url = reverse('user-detail', args=[self.user.pk])
        updated_data = {
            'username': self.test_user_data["username"],
            'email': self.test_user_data["email"],
        }

        response = self.client.put(detail_url, data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_user = CustomUser.objects.get(pk=self.user.pk)
        serialized_data = CustomUserSerializer(updated_user).data
        self.assertEqual(response.data, serialized_data)
        self.assertEqual(updated_user.username, self.test_user_data["username"])
        self.assertEqual(updated_user.email, self.test_user_data["email"])

    def test_user_destroy_api_view_delete(self):

        detail_url = reverse('user-detail', args=[self.user.pk])
        response = self.client.delete(detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ProductViewsTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.fake = Faker()

        self.product = ProductFactory()

    def test_api_view_product_list_get(self):
        list_url = reverse('product-list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_users = Product.objects.all()
        serialized_data = ProductSerializer(expected_users, many=True).data
        self.assertEqual(response.data['count'], len(expected_users))
        self.assertEqual(response.data['next'], None)
        self.assertEqual(response.data['previous'], None)
        self.assertEqual(response.data['results'], serialized_data)
        

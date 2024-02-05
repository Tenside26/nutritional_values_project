
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from users_app.models import CustomUser
from faker import Faker
from api_app.serializers import CustomUserSerializer


class CustomUserListViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('api-users-list')
        self.fake = Faker()

        self.first_user_data = {
            'username': self.fake.user_name(),
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'email': self.fake.email(),
        }

        self.second_user_data = {
            'username': self.fake.user_name(),
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'email': self.fake.email(),
        }

        self.first_user = CustomUser.objects.create(**self.first_user_data)
        self.second_user = CustomUser.objects.create(**self.second_user_data)

    def tearDown(self):
        if hasattr(self, 'first_user') and self.first_user is not None:
            CustomUser.objects.filter(pk=self.first_user.pk).delete()

        if hasattr(self, 'second_user') and self.second_user is not None:
            CustomUser.objects.filter(pk=self.second_user.pk).delete()

        super().tearDown()

    def test_user_list_api_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_users = CustomUser.objects.all()
        serialized_data = CustomUserSerializer(expected_users, many=True).data
        self.assertEqual(response.data, serialized_data)

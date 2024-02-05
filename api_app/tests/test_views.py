
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from users_app.models import CustomUser
from faker import Faker


class CustomUserListViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('user-list')
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

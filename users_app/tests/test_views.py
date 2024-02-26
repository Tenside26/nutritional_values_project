from django.test import TestCase
from rest_framework.test import APIClient
from users_app.factories import CustomUserFactory
from faker import Faker
from django.urls import reverse
from rest_framework import status
from users_app.models import CustomUser


class LoginPageTest(TestCase):
    def setUp(self):
        self.user = CustomUserFactory()
        self.client = APIClient()

    def test_login_view(self):
        data = {'username': self.user.username, 'password': self.user.password}
        response = self.client.post('/login', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)


class RegisterAPIViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.existing_user = CustomUserFactory()
        cls.url = reverse('register')

    def setUp(self):
        self.fake = Faker()
        new_password = self.fake.password(length=40)
        self.input_data = {'username': self.fake.user_name(),
                           'password1': new_password,
                           'password2': new_password,
                           'first_name': self.fake.first_name(),
                           'last_name': self.fake.last_name(),
                           'email': self.fake.email()}

    def test_register_valid_data(self):
        response = self.client.post(self.url, self.input_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = CustomUser.objects.get(username=self.input_data['username'], email=self.input_data['email'])

        self.assertEqual(user.username, self.input_data['username'])
        self.assertEqual(user.first_name, self.input_data['first_name'])
        self.assertEqual(user.last_name, self.input_data['last_name'])
        self.assertEqual(user.email, self.input_data['email'])

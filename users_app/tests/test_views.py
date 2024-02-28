from django.test import TestCase
from rest_framework.test import APIClient
from users_app.factories import CustomUserFactory
from faker import Faker
from django.urls import reverse
from rest_framework import status
from users_app.models import CustomUser
from rest_framework.serializers import ValidationError
from users_app.serializers import RegisterSerializer


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
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        user = CustomUser.objects.get(username=self.input_data['username'], email=self.input_data['email'])

        self.assertEqual(user.username, self.input_data['username'])
        self.assertEqual(user.first_name, self.input_data['first_name'])
        self.assertEqual(user.last_name, self.input_data['last_name'])
        self.assertEqual(user.email, self.input_data['email'])

    def test_register_invalid_data(self):
        self.input_data["username"] = ""
        response = self.client.post(self.url, self.input_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_taken_username(self):
        self.input_data["username"] = self.existing_user.username
        response = self.client.post(self.url, self.input_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        with self.assertRaises(ValidationError) as context:
            serializer = RegisterSerializer(data=self.input_data)
            serializer.is_valid(raise_exception=True)
            self.assertEqual(context.exception.status_code, 202)


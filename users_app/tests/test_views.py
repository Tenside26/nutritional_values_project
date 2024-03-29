from django.test import TestCase
from rest_framework.test import APIClient
from users_app.factories import CustomUserFactory
from faker import Faker
from django.urls import reverse
from rest_framework import status
from users_app.models import CustomUser
from rest_framework.serializers import ValidationError
from users_app.serializers import RegisterSerializer, LoginSerializer


class LoginPageTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('login')
        cls.client = APIClient()
        cls.fake = Faker()
        cls.user = CustomUserFactory()

    def test_login_view_existing_user(self):
        data = {'username': self.user.username, 'password': self.user.password}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)

    def test_login_view_non_existing_user(self):
        data = {'username': self.fake.user_name, 'password': self.fake.password}

        with self.assertRaises(ValidationError) as context:
            serializer = LoginSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.assertEqual(str(context.exception), "Invalid credentials")


class RegisterAPIViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.existing_user = CustomUserFactory()
        cls.url = reverse('register')
        cls.client = APIClient()

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

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual("", self.input_data['username'])

    def test_register_taken_username(self):
        self.input_data["username"] = self.existing_user.username
        response = self.client.post(self.url, self.input_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        with self.assertRaises(ValidationError) as context:
            serializer = RegisterSerializer(data=self.input_data)
            serializer.is_valid(raise_exception=True)
            self.assertEqual(context.exception.status_code, 202)

    def test_register_taken_email(self):
        self.input_data["email"] = self.existing_user.email
        response = self.client.post(self.url, self.input_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        with self.assertRaises(ValidationError) as context:
            serializer = RegisterSerializer(data=self.input_data)
            serializer.is_valid(raise_exception=True)
            self.assertEqual(context.exception.status_code, 202)

    def test_register_password_mismatch(self):
        self.input_data["password1"] = self.fake.password(length=40)
        response = self.client.post(self.url, self.input_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        with self.assertRaises(ValidationError) as context:
            serializer = RegisterSerializer(data=self.input_data)
            serializer.is_valid(raise_exception=True)
            self.assertEqual(str(context.exception), "Passwords do not match.")



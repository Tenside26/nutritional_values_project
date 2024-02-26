
from django.test import TestCase
from users_app.forms import UserRegisterForm
from users_app.models import CustomUser
from django.urls import reverse
from users_app.factories import CustomUserFactory
from faker import Faker


class UserRegisterFormTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.fake = Faker()
        cls.existing_user = CustomUserFactory()
        cls.register_url = reverse('register')

    def setUp(self):
        new_password = self.fake.password(length=40)
        self.form_data = {'username': self.fake.user_name(),
                          'password1': new_password,
                          'password2': new_password,
                          'first_name': self.fake.first_name(),
                          'last_name': self.fake.last_name(),
                          'email': self.fake.email()}

    def test_register_valid_data(self):
        form = UserRegisterForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_register_missing_data(self):
        form_data = {}
        form = UserRegisterForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_register_taken_email(self):
        self.form_data["email"] = self.existing_user.email
        form = UserRegisterForm(data=self.form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('Email already in use', form.errors.get('email', []))

    def test_register_taken_username(self):
        self.form_data["username"] = self.existing_user.username
        form = UserRegisterForm(data=self.form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('Username already taken', form.errors.get('username', []))

    def test_register_password_mismatch(self):
        self.form_data["password2"] = self.fake.password(length=40)
        form = UserRegisterForm(data=self.form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('Passwords do not match', form.errors.get('password1', ['Passwords do not match']))

    def test_register_missing_username(self):
        self.form_data["username"] = ""
        form = UserRegisterForm(data=self.form_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])

    def test_register_missing_password1(self):
        self.form_data["password1"] = ""
        form = UserRegisterForm(data=self.form_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password1'], ['This field is required.'])

    def test_register_missing_password2(self):
        self.form_data["password2"] = ""
        form = UserRegisterForm(data=self.form_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ['This field is required.'])

    def test_register_missing_email(self):
        self.form_data["email"] = ""
        form = UserRegisterForm(data=self.form_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])

    def test_register_user_created_successfully(self):
        response = self.client.post(self.register_url, self.form_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(CustomUser.objects.filter(username=self.form_data["username"]).exists())



from django.test import TestCase
from users_app.forms import UserLoginForm
from django.contrib.auth.models import User


class UserLoginFormTests(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='testuser@example.com',
        )

    def tearDown(self):
        self.test_user.delete()
        super().tearDown()

    def test_valid_data(self):
        form_data = {'username': 'test_user', 'password': 'test_password'}
        form = UserLoginForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form_data = {'username': 'invalid_user', 'password': 'invalid_password'}
        form = UserLoginForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_missing_username(self):
        form_data = {'password': 'test_password'}
        form = UserLoginForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])

    def test_missing_password(self):
        form_data = {'username': 'test_user'}
        form = UserLoginForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], ['This field is required.'])



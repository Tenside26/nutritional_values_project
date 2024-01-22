
from django.test import TestCase
from users_app.forms import UserLoginForm


class UserLoginFormTests(TestCase):
    def test_valid_data(self):
        form_data = {'username': 'testuser', 'password': 'testpassword'}
        form = UserLoginForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_missing_username(self):
        form_data = {'password': 'testpassword'}
        form = UserLoginForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])

    def test_missing_password(self):
        form_data = {'username': 'testuser'}
        form = UserLoginForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], ['This field is required.'])



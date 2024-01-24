
from django.test import TestCase, Client
from users_app.forms import UserLoginForm
from django.contrib.auth.models import User


class UserLoginFormTests(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='testuser@example.com',
        )
        self.client = Client()

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

    def test_wrong_username(self):
        form_data = {'username': 'wrong_user',
                     'password': 'test_password'}

        form = UserLoginForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('Invalid username or password', form.errors['__all__'])

    def test_wrong_password(self):
        form_data = {'username': 'test_user',
                     'password': 'wrong_password'}

        form = UserLoginForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('Invalid username or password', form.errors['__all__'])

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

    def test_missing_data(self):
        form_data = {}
        form = UserLoginForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_successful_login(self):
        form_data = {'username': 'test_user', 'password': 'test_password'}
        response = self.client.post('', form_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn('_auth_user_id', self.client.session)

        user_id = self.client.session['_auth_user_id']
        logged_in_user = User.objects.get(id=user_id)

        self.assertEqual(logged_in_user, self.test_user)




from django.test import TestCase, Client
from users_app.forms import UserLoginForm, UserRegisterForm
from users_app.models import CustomUser
from django.urls import reverse
from users_app.factories import CustomUserFactory
from faker import Faker


class UserLoginFormTests(TestCase):

    def setUp(self):
        self.test_user = CustomUserFactory()
        self.client = Client()

    def test_login_valid_data(self):
        form_data = {'username': self.test_user.username,
                     'password': self.test_user.password}

        form = UserLoginForm(data=form_data)
        if not form.is_valid():
            print(form.errors)

        self.assertTrue(form.is_valid())

    def test_login_invalid_data(self):
        form_data = {'username': 'invalid_user',
                     'password': 'invalid_password'}

        form = UserLoginForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_login_wrong_username(self):
        form_data = {'username': 'wrong_user',
                     'password': self.test_user.password}

        form = UserLoginForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('Invalid username or password', form.errors['__all__'])

    def test_login_wrong_password(self):
        form_data = {'username': self.test_user.username,
                     'password': 'wrong_password'}

        form = UserLoginForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('Invalid username or password', form.errors['__all__'])

    def test_login_missing_username(self):
        form_data = {'password': self.test_user.password}

        form = UserLoginForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])

    def test_login_missing_password(self):
        form_data = {'username': self.test_user.username}

        form = UserLoginForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], ['This field is required.'])

    def test_login_missing_data(self):
        form_data = {}
        form = UserLoginForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_login_successful_login(self):
        form_data = {'username': self.test_user.username,
                     'password': self.test_user.password}

        response = self.client.post('', form_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('calculator'))
        self.assertIn('_auth_user_id', self.client.session)

        user_id = self.client.session['_auth_user_id']
        logged_in_user = CustomUser.objects.get(id=user_id)

        self.assertEqual(logged_in_user, self.test_user)


class UserRegisterFormTests(TestCase):

    def setUp(self):
        self.fake = Faker()
        self.existing_user = CustomUserFactory()
        self.register_url = reverse('register')

    def test_register_valid_data(self):
        new_password = self.fake.password(length=40)
        form_data = {'username': self.fake.user_name(),
                     'password1': new_password,
                     'password2': new_password,
                     'first_name': self.fake.first_name(),
                     'last_name': self.fake.last_name(),
                     'email': self.fake.email()}

        form = UserRegisterForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_register_missing_data(self):
        form_data = {}

        form = UserRegisterForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_register_taken_email(self):
        new_password = self.fake.password(length=40)
        form_data = {'username': self.fake.user_name(),
                     'password1': new_password,
                     'password2': new_password,
                     'first_name': self.fake.first_name(),
                     'last_name': self.fake.last_name(),
                     'email': self.existing_user.email}

        form = UserRegisterForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('Email already in use', form.errors.get('email', []))

    def test_register_taken_username(self):
        new_password = self.fake.password(length=40)
        form_data = {'username': self.existing_user.username,
                     'password1': new_password,
                     'password2': new_password,
                     'first_name': self.fake.first_name(),
                     'last_name': self.fake.last_name(),
                     'email': self.fake.email()}

        form = UserRegisterForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('Username already taken', form.errors.get('username', []))

    def test_register_password_mismatch(self):
        form_data = {'username': self.fake.user_name(),
                     'password1': self.fake.password(length=40),
                     'password2': 'wrong_password',
                     'first_name': self.fake.first_name(),
                     'last_name': self.fake.last_name(),
                     'email': self.fake.email()}

        form = UserRegisterForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('Passwords do not match', form.errors.get('password1', ['Passwords do not match']))

    def test_register_missing_username(self):
        new_password = self.fake.password(length=40)
        form_data = {'password1': new_password,
                     'password2': new_password,
                     'first_name': self.fake.first_name(),
                     'last_name': self.fake.last_name(),
                     'email': self.fake.email()}

        form = UserRegisterForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])

    def test_register_missing_password1(self):
        form_data = {'username': self.fake.user_name(),
                     'password2': self.fake.password(length=40),
                     'first_name': self.fake.first_name(),
                     'last_name': self.fake.last_name(),
                     'email': self.fake.email()}

        form = UserRegisterForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password1'], ['This field is required.'])

    def test_register_missing_password2(self):
        form_data = {'username': self.fake.user_name(),
                     'password1': self.fake.password(length=40),
                     'first_name': self.fake.first_name(),
                     'last_name': self.fake.last_name(),
                     'email': self.fake.email()}

        form = UserRegisterForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ['This field is required.'])

    def test_register_missing_email(self):
        new_password = self.fake.password(length=40)
        form_data = {'username': self.fake.user_name(),
                     'password1': new_password,
                     'password2': new_password,
                     'first_name': self.fake.first_name(),
                     'last_name': self.fake.last_name()}

        form = UserRegisterForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])

    def test_register_user_created_successfully(self):
        new_password = self.fake.password(length=40)
        new_username = self.fake.user_name()
        form_data = {'username': new_username,
                     'password1': new_password,
                     'password2': new_password,
                     'first_name': self.fake.first_name(),
                     'last_name': self.fake.last_name(),
                     'email': self.fake.email()}

        response = self.client.post(self.register_url, form_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(CustomUser.objects.filter(username=new_username).exists())


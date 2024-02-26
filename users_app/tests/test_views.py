from django.test import TestCase
from django.urls import reverse, resolve
from users_app.forms import UserRegisterForm
from users_app.views import register_page
from rest_framework.test import APIClient
from users_app.factories import CustomUserFactory


class LoginPageTest(TestCase):
    def setUp(self):
        self.user = CustomUserFactory()
        self.client = APIClient()

    def test_login_view(self):
        data = {'username': self.user.username, 'password': self.user.password}
        response = self.client.post('/login', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)


class RegisterPageTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')

    def test_register_page_template_render_correctly(self):
        response = self.client.get(self.register_url)

        self.assertTemplateUsed(response,'register.html')

    def test_register_page_url(self):
        found = resolve('/register')
        self.assertEqual(found.func, register_page)

    def test_register_page_renders_correct_form(self):
        response = self.client.post(self.register_url)

        self.assertIsInstance(response.context['form'], UserRegisterForm)

from django.test import TestCase
from django.urls import reverse, resolve
from users_app.forms import UserLoginForm, UserRegisterForm
from users_app.views import login_page, register_page


class LoginPageTest(TestCase):
    def setUp(self):
        self.login_url = reverse('login')

    def test_login_page_template_render_correctly(self):
        response = self.client.get(self.login_url)

        self.assertTemplateUsed(response,'login.html')

    def test_login_page_url(self):
        found = resolve('/')
        self.assertEqual(found.func, login_page)

    def test_login_page_renders_correct_form(self):
        response = self.client.post(self.login_url)

        self.assertIsInstance(response.context['form'], UserLoginForm)


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

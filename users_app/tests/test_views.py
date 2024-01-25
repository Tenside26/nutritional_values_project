from django.test import TestCase
from users_app.models import CustomUser
from django.urls import reverse
from users_app.forms import UserLoginForm


class LoginPageTest(TestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.user = CustomUser.objects.create_user(username='test_user', password='test_password')

    def tearDown(self):
        self.user.delete()

    def test_login_page_template_render_correctly(self):
        response = self.client.get(self.login_url)

        self.assertTemplateUsed(response,'login.html')

    def test_login_page_renders_correct_form(self):
        response = self.client.get(self.login_url)

        self.assertIsInstance(response.context['form'], UserLoginForm)
        self.assertContains(response, '<form method="post" action="{}">'.format(self.login_url), html=True)
        self.assertContains(response, 'csrfmiddlewaretoken', html=True)


class RegisterPageTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.user = CustomUser.objects.create_user(username='test_user',
                                                   password='test_password',
                                                   first_name='test_first',
                                                   last_name='test_last',
                                                   email='test@example.com')

    def tearDown(self):
        self.user.delete()

    def test_register_page_template_render_correctly(self):
        response = self.client.get(self.register_url)

        self.assertTemplateUsed(response,'register.html')

from django.test import TestCase
from users_app.models import CustomUser
from django.urls import reverse



class LoginPageTest(TestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.user = CustomUser.objects.create_user(username='test_user', password='test_password')

    def tearDown(self):
        self.user.delete()

    def test_login_page_successful(self):
        data = {'username': 'test_user', 'password': 'test_password'}
        response = self.client.post(self.login_url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('calculator'))

    def test_login_page_unsuccessful(self):
        data = {'username': 'test_user', 'password': 'wrong_password'}
        response = self.client.post(self.login_url, data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password')

    def test_login_page_template_render_correctly(self):
        response = self.client.get(self.login_url)

        self.assertTemplateUsed(response,'login.html')


from django.test import TestCase
from api_app.serializers import CustomUserSerializer
from users_app.models import CustomUser
from faker import Faker


class CustomUserSerializerTests(TestCase):

    def setUp(self):
        self.fake = Faker()
        new_password = self.fake.password(length=40)
        self.user_data = {
            'username': self.fake.user_name(),
            'password1': new_password,
            'password2': new_password,
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'email': self.fake.email(),
        }
        self.user_instance = CustomUser.objects.create(**self.user_data)
        self.serializer = CustomUserSerializer(instance=self.user_instance)

    def tearDown(self):
        if self.user_instance:
            self.user_instance.delete()
        super().tearDown()


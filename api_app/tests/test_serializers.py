from django.test import TestCase
from api_app.serializers import CustomUserSerializer
from users_app.models import CustomUser
from faker import Faker


class CustomUserSerializerTests(TestCase):

    def setUp(self):
        self.fake = Faker()
        self.user_data = {
            'username': self.fake.user_name(),
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

    def test_user_serialization(self):
        serialized_data = self.serializer.data

        self.assertEqual(serialized_data['username'], self.user_data['username'])
        self.assertEqual(serialized_data['first_name'], self.user_data['first_name'])
        self.assertEqual(serialized_data['last_name'], self.user_data['last_name'])
        self.assertEqual(serialized_data['email'], self.user_data['email'])
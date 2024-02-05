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
        self.serializer_input_data = {
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
        if hasattr(self, 'created_instance'):
            self.created_instance.delete()
        super().tearDown()

    def test_user_serialization(self):
        serialized_data = self.serializer.data

        self.assertEqual(serialized_data['username'], self.user_data['username'])
        self.assertEqual(serialized_data['first_name'], self.user_data['first_name'])
        self.assertEqual(serialized_data['last_name'], self.user_data['last_name'])
        self.assertEqual(serialized_data['email'], self.user_data['email'])

    def test_user_deserialization(self):

        serializer = CustomUserSerializer(data=self.serializer_input_data)
        self.assertTrue(serializer.is_valid())

        instance = serializer.save()
        self.created_instance = instance
        saved_instance = CustomUser.objects.get(pk=instance.pk)

        self.assertEqual(saved_instance.username, self.serializer_input_data['username'])
        self.assertEqual(saved_instance.first_name, self.serializer_input_data['first_name'])
        self.assertEqual(saved_instance.last_name, self.serializer_input_data['last_name'])
        self.assertEqual(saved_instance.email, self.serializer_input_data['email'])
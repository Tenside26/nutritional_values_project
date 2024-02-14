from django.test import TestCase
from api_app.serializers import CustomUserSerializer
from users_app.models import CustomUser
from faker import Faker
from users_app.factories import CustomUserFactory


class CustomUserSerializerTests(TestCase):

    def setUp(self):
        self.fake = Faker()
        self.user_data = CustomUserFactory()
        self.serializer_input_data = {
            'username': self.fake.user_name(),
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'email': self.fake.email(),
        }
        self.serializer = CustomUserSerializer(instance=self.user_data)

    def tearDown(self):

        if hasattr(self, 'created_instance'):
            self.created_instance.delete()

        super().tearDown()

    def test_user_serialization(self):
        serialized_data = self.serializer.data

        self.assertEqual(serialized_data['username'], self.user_data.username)
        self.assertEqual(serialized_data['first_name'], self.user_data.first_name)
        self.assertEqual(serialized_data['last_name'], self.user_data.last_name)
        self.assertEqual(serialized_data['email'], self.user_data.email)

    def test_user_deserialization(self):

        serializer = CustomUserSerializer(data=self.serializer_input_data)
        self.assertTrue(serializer.is_valid())

        instance = serializer.save()
        self.created_instance = instance
        saved_instance = CustomUser.objects.get(pk=self.created_instance.pk)

        self.assertEqual(saved_instance.username, self.serializer_input_data['username'])
        self.assertEqual(saved_instance.first_name, self.serializer_input_data['first_name'])
        self.assertEqual(saved_instance.last_name, self.serializer_input_data['last_name'])
        self.assertEqual(saved_instance.email, self.serializer_input_data['email'])

    def test_user_serialization_wrong_username(self):
        serialized_data = self.serializer.data

        self.assertNotEqual(serialized_data['username'],  self.fake.user_name())
        self.assertEqual(serialized_data['first_name'], self.user_data.first_name)
        self.assertEqual(serialized_data['last_name'], self.user_data.last_name)
        self.assertEqual(serialized_data['email'], self.user_data.email)

    def test_user_serialization_wrong_first_name(self):
        serialized_data = self.serializer.data

        self.assertEqual(serialized_data['username'], self.user_data.username)
        self.assertNotEqual(serialized_data['first_name'],  self.fake.first_name())
        self.assertEqual(serialized_data['last_name'], self.user_data.last_name)
        self.assertEqual(serialized_data['email'], self.user_data.email)

    def test_user_serialization_wrong_last_name(self):
        serialized_data = self.serializer.data

        self.assertEqual(serialized_data['username'], self.user_data.username)
        self.assertEqual(serialized_data['first_name'], self.user_data.first_name)
        self.assertNotEqual(serialized_data['last_name'],  self.fake.last_name())
        self.assertEqual(serialized_data['email'], self.user_data.email)

    def test_user_serialization_wrong_email(self):
        serialized_data = self.serializer.data

        self.assertEqual(serialized_data['username'], self.user_data.username)
        self.assertEqual(serialized_data['first_name'], self.user_data.first_name)
        self.assertEqual(serialized_data['last_name'], self.user_data.last_name)
        self.assertNotEqual(serialized_data['email'], self.fake.email())

    def test_user_serialization_missing_data(self):
        serialized_data = CustomUserSerializer(data={})

        self.assertFalse(serialized_data.is_valid())
        self.assertIsNone(serialized_data.validated_data.get('username'))
        self.assertIsNone(serialized_data.validated_data.get('first_name'))
        self.assertIsNone(serialized_data.validated_data.get('last_name'))
        self.assertIsNone(serialized_data.validated_data.get('email'))

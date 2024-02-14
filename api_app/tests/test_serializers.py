from django.test import TestCase
from api_app.serializers import CustomUserSerializer, ProductSerializer
from users_app.models import CustomUser
from calculator_app.models import Product
from faker import Faker
from users_app.factories import CustomUserFactory
from calculator_app.factories import ProductFactory


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


class ProductSerializerTests(TestCase):

    def setUp(self):
        self.fake = Faker()
        self.product_data = ProductFactory()
        self.serializer_input_data = {
            'name': self.fake.text(max_nb_chars=255),
            'serving_size': self.fake.random_int(min=1, max=5000),
            'calories': self.fake.random_int(min=1, max=10000),
            'protein': self.fake.pyfloat(left_digits=2, right_digits=2, positive=True),
            'carbohydrate': self.fake.pyfloat(left_digits=2, right_digits=2, positive=True),
            'fat': self.fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        }

        self.serializer = ProductSerializer(instance=self.product_data)

    def tearDown(self):

        if hasattr(self, 'created_instance'):
            self.created_instance.delete()

        super().tearDown()

    def test_product_serialization(self):
        serialized_data = self.serializer.data

        self.assertEqual(serialized_data['name'], self.product_data.name)
        self.assertEqual(serialized_data['serving_size'], self.product_data.serving_size)
        self.assertEqual(serialized_data['calories'], self.product_data.calories)
        self.assertEqual(serialized_data['protein'], self.product_data.protein)
        self.assertEqual(serialized_data['carbohydrate'], self.product_data.carbohydrate)
        self.assertEqual(serialized_data['fat'], self.product_data.fat)

    def test_product_deserialization(self):
        serializer = ProductSerializer(data=self.serializer_input_data)
        self.assertTrue(serializer.is_valid())

        instance = serializer.save()
        self.created_instance = instance
        saved_instance = Product.objects.get(pk=self.created_instance.pk)

        self.assertEqual(saved_instance.name, self.serializer_input_data['name'])
        self.assertEqual(saved_instance.serving_size, self.serializer_input_data['serving_size'])
        self.assertEqual(saved_instance.calories, self.serializer_input_data['calories'])
        self.assertEqual(saved_instance.protein, self.serializer_input_data['protein'])
        self.assertEqual(saved_instance.carbohydrate, self.serializer_input_data['carbohydrate'])
        self.assertEqual(saved_instance.fat, self.serializer_input_data['fat'])

    def test_product_serialization_wrong_name(self):
        serialized_data = self.serializer.data

        self.assertNotEqual(serialized_data['name'],  self.fake.text(max_nb_chars=255))
        self.assertEqual(serialized_data['serving_size'], self.product_data.serving_size)
        self.assertEqual(serialized_data['calories'], self.product_data.calories)
        self.assertEqual(serialized_data['protein'], self.product_data.protein)
        self.assertEqual(serialized_data['carbohydrate'], self.product_data.carbohydrate)
        self.assertEqual(serialized_data['fat'], self.product_data.fat)

    def test_product_serialization_wrong_serving_size(self):
        serialized_data = self.serializer.data

        self.assertEqual(serialized_data['name'],  self.product_data.name)
        self.assertNotEqual(serialized_data['serving_size'], self.fake.random_int(min=1, max=5000))
        self.assertEqual(serialized_data['calories'], self.product_data.calories)
        self.assertEqual(serialized_data['protein'], self.product_data.protein)
        self.assertEqual(serialized_data['carbohydrate'], self.product_data.carbohydrate)
        self.assertEqual(serialized_data['fat'], self.product_data.fat)

    def test_product_serialization_wrong_calories(self):
        serialized_data = self.serializer.data

        self.assertEqual(serialized_data['name'],  self.product_data.name)
        self.assertEqual(serialized_data['serving_size'], self.product_data.serving_size)
        self.assertNotEqual(serialized_data['calories'], self.fake.random_int(min=1, max=10000))
        self.assertEqual(serialized_data['protein'], self.product_data.protein)
        self.assertEqual(serialized_data['carbohydrate'], self.product_data.carbohydrate)
        self.assertEqual(serialized_data['fat'], self.product_data.fat)


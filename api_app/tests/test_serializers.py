from django.test import TestCase
from api_app.serializers import CustomUserSerializer, ProductSerializer
from users_app.models import CustomUser
from calculator_app.models import Product
from faker import Faker
from users_app.factories import CustomUserFactory
from calculator_app.factories import ProductFactory


class CustomUserSerializerTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.fake = Faker()
        cls.user_data = CustomUserFactory()
        cls.serializer = CustomUserSerializer(instance=cls.user_data)
        cls.serializer_input_data = {
            'username': cls.fake.user_name(),
            'first_name': cls.fake.first_name(),
            'last_name': cls.fake.last_name(),
            'email': cls.fake.email(),
        }

    def test_user_serialization(self):
        self.assertEqual(self.serializer.data['username'], self.user_data.username)
        self.assertEqual(self.serializer.data['first_name'], self.user_data.first_name)
        self.assertEqual(self.serializer.data['last_name'], self.user_data.last_name)
        self.assertEqual(self.serializer.data['email'], self.user_data.email)

    def test_user_deserialization(self):
        serializer = CustomUserSerializer(data=self.serializer_input_data)
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()

        saved_instance = CustomUser.objects.get(pk=instance.pk)

        self.assertEqual(saved_instance.username, self.serializer_input_data['username'])
        self.assertEqual(saved_instance.first_name, self.serializer_input_data['first_name'])
        self.assertEqual(saved_instance.last_name, self.serializer_input_data['last_name'])
        self.assertEqual(saved_instance.email, self.serializer_input_data['email'])

    def test_user_serialization_wrong_username(self):
        self.assertNotEqual(self.serializer.data['username'],  self.fake.user_name())

    def test_user_serialization_wrong_first_name(self):
        self.assertNotEqual(self.serializer.data['first_name'],  self.fake.first_name())

    def test_user_serialization_wrong_last_name(self):
        self.assertNotEqual(self.serializer.data['last_name'],  self.fake.last_name())

    def test_user_serialization_wrong_email(self):
        self.assertNotEqual(self.serializer.data['email'], self.fake.email())

    def test_user_serialization_missing_data(self):
        serialized_data = CustomUserSerializer(data={})

        self.assertFalse(serialized_data.is_valid())
        self.assertIsNone(serialized_data.validated_data.get('username'))
        self.assertIsNone(serialized_data.validated_data.get('first_name'))
        self.assertIsNone(serialized_data.validated_data.get('last_name'))
        self.assertIsNone(serialized_data.validated_data.get('email'))


class ProductSerializerTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.fake = Faker()
        cls.product_data = ProductFactory()
        cls.serializer = ProductSerializer(instance=cls.product_data)
        cls.serializer_input_data = {
            'name': cls.fake.word(),
            'serving_size': cls.fake.random_int(min=1, max=5000),
            'calories': cls.fake.random_int(min=1, max=10000),
            'protein': cls.fake.pyfloat(left_digits=2, right_digits=2, positive=True),
            'carbohydrate': cls.fake.pyfloat(left_digits=2, right_digits=2, positive=True),
            'fat': cls.fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        }

    def test_product_serialization(self):
        self.assertEqual(self.serializer.data['name'], self.product_data.name)
        self.assertEqual(self.serializer.data['serving_size'], self.product_data.serving_size)
        self.assertEqual(self.serializer.data['calories'], self.product_data.calories)
        self.assertEqual(self.serializer.data['protein'], self.product_data.protein)
        self.assertEqual(self.serializer.data['carbohydrate'], self.product_data.carbohydrate)
        self.assertEqual(self.serializer.data['fat'], self.product_data.fat)

    def test_product_deserialization(self):
        serializer = ProductSerializer(data=self.serializer_input_data)
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()

        saved_instance = Product.objects.get(pk=instance.pk)

        self.assertEqual(saved_instance.name, self.serializer_input_data['name'])
        self.assertEqual(saved_instance.serving_size, self.serializer_input_data['serving_size'])
        self.assertEqual(saved_instance.calories, self.serializer_input_data['calories'])
        self.assertEqual(saved_instance.protein, self.serializer_input_data['protein'])
        self.assertEqual(saved_instance.carbohydrate, self.serializer_input_data['carbohydrate'])
        self.assertEqual(saved_instance.fat, self.serializer_input_data['fat'])

    def test_product_serialization_incorrect_name_data(self):
        self.assertNotEqual(self.serializer.data['name'], self.fake.text(max_nb_chars=255))

    def test_product_serialization_incorrect_serving_size_data(self):
        self.assertNotEqual(self.serializer.data['serving_size'], self.fake.random_int(min=1, max=5000))

    def test_product_serialization_incorrect_calories_data(self):
        self.assertNotEqual(self.serializer.data['calories'], self.fake.random_int(min=1, max=10000))

    def test_product_serialization_incorrect_protein_data(self):
        self.assertNotEqual(self.serializer.data['protein'], self.fake.pyfloat(left_digits=2,
                                                                               right_digits=2,
                                                                               positive=True))

    def test_product_serialization_incorrect_carbohydrate_data(self):
        self.assertNotEqual(self.serializer.data['carbohydrate'], self.fake.pyfloat(left_digits=2,
                                                                                    right_digits=2,
                                                                                    positive=True))

    def test_product_serialization_incorrect_fat_data(self):
        self.assertNotEqual(self.serializer.data['fat'], self.fake.pyfloat(left_digits=2,
                                                                           right_digits=2,
                                                                           positive=True))

    def test_product_serialization_missing_data(self):
        serialized_data = ProductSerializer(data={})

        self.assertFalse(serialized_data.is_valid())
        self.assertIsNone(serialized_data.validated_data.get('name'))
        self.assertIsNone(serialized_data.validated_data.get('serving_size'))
        self.assertIsNone(serialized_data.validated_data.get('calories'))
        self.assertIsNone(serialized_data.validated_data.get('protein'))
        self.assertIsNone(serialized_data.validated_data.get('carbohydrate'))
        self.assertIsNone(serialized_data.validated_data.get('fat'))


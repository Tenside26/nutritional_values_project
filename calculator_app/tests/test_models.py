from django.test import TestCase
from calculator_app.factories import ProductFactory
from calculator_app.models import Product
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from faker import Faker


class ProductModelTests(TestCase):

    def setUp(self):
        self.product = ProductFactory()
        self.fake = Faker()

    def test_product_model_create_product(self):
        self.assertIsInstance(self.product, Product)
        self.assertIsNotNone(self.product.pk)
        self.assertIsNotNone(self.product.name)
        self.assertIsNotNone(self.product.serving_size)
        self.assertIsNotNone(self.product.calories)
        self.assertIsNotNone(self.product.protein)
        self.assertIsNotNone(self.product.carbohydrate)
        self.assertIsNotNone(self.product.fat)

    def test_product_model_name_char_field(self):
        with self.assertRaises(ValidationError):
            self.product.name = self.fake.random_int()
            self.product.full_clean()

    def test_product_model_name_max_length(self):
        with self.assertRaises(ValidationError):
            self.product.name = 'a' * 256
            self.product.full_clean()

    def test_product_model_name_unique_constraint(self):
        with self.assertRaises(IntegrityError):
            product_with_same_name = ProductFactory(name=self.product.name)
            product_with_same_name.save()

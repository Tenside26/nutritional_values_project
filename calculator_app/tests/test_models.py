from django.test import TestCase
from calculator_app.factories import ProductFactory
from calculator_app.models import Product
from django.core.exceptions import ValidationError


class ProductModelTests(TestCase):

    def setUp(self):
        self.product = ProductFactory()

    def test_product_model_create_product(self):
        self.assertIsInstance(self.product, Product)
        self.assertIsNotNone(self.product.pk)
        self.assertIsNotNone(self.product.name)
        self.assertIsNotNone(self.product.serving_size)
        self.assertIsNotNone(self.product.calories)
        self.assertIsNotNone(self.product.protein)
        self.assertIsNotNone(self.product.carbohydrate)
        self.assertIsNotNone(self.product.fat)

    def test_product_model_name_max_length(self):
        self.product.name = 'a' * 256
        self.assertRaises(ValidationError, self.product.full_clean)

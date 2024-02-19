from django.test import TestCase
from calculator_app.factories import ProductFactory
from calculator_app.models import Product


class ProductModelTests(TestCase):

    def setUp(self):
        self.product = ProductFactory()

    def test_create_product(self):
        self.assertIsInstance(self.product, Product)
        self.assertIsNotNone(self.product.pk)
        self.assertIsNotNone(self.product.name)
        self.assertIsNotNone(self.product.serving_size)
        self.assertIsNotNone(self.product.calories)
        self.assertIsNotNone(self.product.protein)
        self.assertIsNotNone(self.product.carbohydrate)
        self.assertIsNotNone(self.product.fat)

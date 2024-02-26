from django.test import TestCase
from calculator_app.factories import ProductFactory, MealFactory, CustomUserFactory
from calculator_app.models import Product, Meal, CustomUser
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from faker import Faker


class ProductModelTests(TestCase):

    def setUp(self):
        self.fake = Faker()
        self.product = ProductFactory()

    def test_product_model_create(self):
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

    def test_product_model_name_null_constraint(self):
        with self.assertRaises(IntegrityError):
            null_field = ProductFactory(name=None)
            null_field.save()

    def test_product_model_serving_size_field(self):
        with self.assertRaises(ValidationError):
            self.product.serving_size = self.fake.word()
            self.product.full_clean()

    def test_product_model_calories_field(self):
        with self.assertRaises(ValidationError):
            self.product.calories = self.fake.word()
            self.product.full_clean()

    def test_product_model_protein_field(self):
        with self.assertRaises(ValidationError):
            self.product.protein = self.fake.word()
            self.product.full_clean()

    def test_product_model_carbohydrate_field(self):
        with self.assertRaises(ValidationError):
            self.product.carbohydrate = self.fake.word()
            self.product.full_clean()

    def test_product_model_fat_field(self):
        with self.assertRaises(ValidationError):
            self.product.fat = self.fake.word()
            self.product.full_clean()


class MealModelTests(TestCase):

    def setUp(self):
        self.fake = Faker()
        self.product = ProductFactory()
        self.user = CustomUserFactory()
        self.meal = MealFactory(user=self.user, product=self.product)
        self.meal.product.set([self.product])

    def test_meal_model_create(self):
        self.assertIsInstance(self.meal, Meal)
        self.assertEqual(self.meal.user, self.user)
        self.assertEqual(self.meal.product.count(), 1)
        self.assertIn(self.product, self.meal.product.all())

    def test_meal_model_with_multiple_products(self):
        self.new_product = ProductFactory()
        self.meal.product.add(self.new_product)

        self.assertEqual(self.meal.product.count(), 2)
        self.assertIn(self.product, self.meal.product.all())
        self.assertIn(self.new_product, self.meal.product.all())

    def test_meal_model_related_name_for_user(self):
        self.assertIn(self.meal, self.user.meal_user.all())

    def test_meal_model_remove_product_from_meal(self):
        self.meal.product.remove(self.product)

        self.assertEqual(self.meal.product.count(), 0)
        self.assertNotIn(self.product, self.meal.product.all())

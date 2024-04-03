import factory
from calculator_app.models import Product, Meal
from users_app.factories import CustomUserFactory


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    serving_size = factory.Faker('random_int', min=1, max=5000)
    calories = factory.Faker('random_int', min=1, max=10000)
    protein = factory.Faker('pyfloat', left_digits=2, right_digits=2, positive=True)
    carbohydrate = factory.Faker('pyfloat', left_digits=2, right_digits=2, positive=True)
    fat = factory.Faker('pyfloat', left_digits=2, right_digits=2, positive=True)


class MealFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Meal

    title = factory.Faker('word')
    user = factory.SubFactory(CustomUserFactory)
    product = factory.RelatedFactoryList(ProductFactory, factory_related_name='meal')
    date = factory.Faker("date_time_this_decade")



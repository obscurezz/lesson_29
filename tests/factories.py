import factory.django
from factory import SubFactory, fuzzy, Faker, RelatedFactory

from ads.models import Ad, Selection
from authentication.models import User
from basics.models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker(provider='name')
    slug = fuzzy.FuzzyText(length=10)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker(provider='name')
    password = factory.Faker(provider='password')
    email = factory.Faker(provider='email')
    age = 18
    role = 'ADMIN'


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = factory.Faker(provider='name')
    author = RelatedFactory(UserFactory)
    category = RelatedFactory(CategoryFactory)
    price = 1000
    description = None
    is_published = False


class SelectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Selection

    name = factory.Faker(provider='name')
    owner = SubFactory(UserFactory)
    items = None

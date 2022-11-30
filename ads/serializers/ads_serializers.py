from rest_framework.serializers import ModelSerializer, SlugRelatedField, IntegerField, BooleanField
from ads.models import Ad
from ads.validators import IsPublishedNotTrueValidator
from basics.serializers.cats_serializer import CategoriesSerializer
from authentication.serializers.users_serializer import UsersRetrieveSerializer


class AdsListSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    category = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Ad
        fields = ['id', 'author', 'name', 'price', 'is_published', 'category', 'location']


class AdsRetrieveSerializer(ModelSerializer):
    author = UsersRetrieveSerializer(read_only=True)
    category = CategoriesSerializer(read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'


class AdsCreateSerializer(ModelSerializer):
    id = IntegerField(required=False)
    is_published = BooleanField(required=False, default=False, validators=[IsPublishedNotTrueValidator()])

    class Meta:
        model = Ad
        exclude = ['author', 'category']


class AdsDeleteUpdateSerializer(ModelSerializer):
    id = IntegerField(required=False)

    class Meta:
        model = Ad
        exclude = ['author', 'category']

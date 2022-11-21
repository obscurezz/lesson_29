from rest_framework.serializers import ModelSerializer, SlugRelatedField, IntegerField
from ads.models import User
from ads.serializers.locs_serializer import LocationsSerializer


class UsersListSerializer(ModelSerializer):
    location = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'location']


class UsersRetrieveSerializer(ModelSerializer):
    location = LocationsSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class UsersCUDSerializer(ModelSerializer):
    id = IntegerField(required=False)

    class Meta:
        model = User
        exclude = ['location']

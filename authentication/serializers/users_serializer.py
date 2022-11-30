from rest_framework.serializers import ModelSerializer, SlugRelatedField, IntegerField, DateField, CharField
from authentication.models import User
from authentication.validators import MinAgeValidator, CheckEmailNotDomainValidator
from basics.serializers.locs_serializer import LocationsSerializer


class UsersListSerializer(ModelSerializer):
    location = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'location']


class UsersRetrieveSerializer(ModelSerializer):
    location = LocationsSerializer(read_only=True)

    class Meta:
        model = User
        exclude = ['password']


class UsersCreateSerializer(ModelSerializer):
    id = IntegerField(required=False)
    birth_date = DateField(validators=[MinAgeValidator(9)])
    email = CharField(required=False, validators=[CheckEmailNotDomainValidator('rambler.ru')])

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        return user


class UsersDeleteUpdateSerializer(ModelSerializer):
    id = IntegerField(required=False)

    class Meta:
        model = User
        fields = ['username']

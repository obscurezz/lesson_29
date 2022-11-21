from rest_framework.serializers import ModelSerializer
from ads.models import Location


class LocationsSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

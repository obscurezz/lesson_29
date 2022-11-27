from rest_framework.viewsets import ModelViewSet

from basics.models import Location
from basics.serializers.locs_serializer import LocationsSerializer


class LocationsViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationsSerializer

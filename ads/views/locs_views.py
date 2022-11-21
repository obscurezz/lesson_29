from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from ads.models import Location
from ads.serializers.locs_serializer import LocationsSerializer


class LocationsViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationsSerializer

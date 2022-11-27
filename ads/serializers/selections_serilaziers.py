from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, IntegerField

from ads.models import Selection
from ads.serializers.ads_serializers import AdsListSerializer


class SelectionsListSerializer(ModelSerializer):
    class Meta:
        model = Selection
        exclude = ['owner']


class SelectionsDetailSerializer(ModelSerializer):
    items = AdsListSerializer(many=True)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionsCreateSerializer(ModelSerializer):
    id = IntegerField(required=False)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionsUpdateDeleteSerializer(ModelSerializer):
    owner = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Selection
        fields = '__all__'

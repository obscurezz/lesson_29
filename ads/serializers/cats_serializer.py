from rest_framework.serializers import ModelSerializer
from ads.models import Category


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

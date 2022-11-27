from rest_framework.serializers import ModelSerializer
from basics.models import Category


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

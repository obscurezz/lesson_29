from rest_framework.viewsets import ModelViewSet

from basics.models import Category
from basics.serializers.cats_serializer import CategoriesSerializer


class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer

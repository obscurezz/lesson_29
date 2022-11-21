from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from ads.models import Category
from ads.serializers.cats_serializer import CategoriesSerializer


class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer

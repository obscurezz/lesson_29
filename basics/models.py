from django.core.validators import MinValueValidator
from django.db import models
from base_model import BaseModel


class Location(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    lat = models.FloatField(default=0.0)
    lng = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=10, unique=True, validators=[MinValueValidator(5)], null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

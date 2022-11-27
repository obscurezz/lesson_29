from django.db import models
from base_model import BaseModel
from authentication.models import User
from basics.models import Category


class Ad(BaseModel):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=4000)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='logos/', default='logos/logo.png')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    @property
    def get_image_url(self):
        return self.image.url

    @property
    def username(self):
        return self.author.username if self.author else None

    @property
    def location(self):
        return self.author.location.name

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-price']

    def __str__(self):
        return self.name


class Selection(BaseModel):
    name = models.CharField(max_length=30, unique=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    @property
    def owner_name(self):
        return self.owner.username

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"
        ordering = ['name']

    def __repr__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import AbstractUser
from basics.models import Location


class User(AbstractUser):
    ADMIN = 'Admin'
    USER = 'User'
    MODERATOR = 'Moderator'
    ROLES = [(ADMIN, ADMIN), (USER, USER), (MODERATOR, MODERATOR)]

    age = models.PositiveIntegerField(default=18)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=10, choices=ROLES, default=USER)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

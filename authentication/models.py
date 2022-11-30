import datetime
from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractUser
from basics.models import Location


class User(AbstractUser):
    ADMIN = 'Admin'
    USER = 'User'
    MODERATOR = 'Moderator'
    ROLES = [(ADMIN, ADMIN), (USER, USER), (MODERATOR, MODERATOR)]

    age = models.PositiveIntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=10, choices=ROLES, default=USER)
    birth_date = models.DateField(null=False, default=(date.today() - datetime.timedelta(days=365*9)))

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

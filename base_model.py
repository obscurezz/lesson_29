from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    id = models.AutoField(primary_key=True)

    def __str__(self):
        if hasattr(self, "name"):
            return self.name
        if hasattr(self, "username"):
            return self.username

    class Meta:
        abstract = True

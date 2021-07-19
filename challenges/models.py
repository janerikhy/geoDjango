from django.db import models
from users.models import CitizenScientist


class Challange(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    max_points = models.IntegerField(default=10)
    users = models.ManyToManyField(CitizenScientist)

    def __str__(self) -> str:
        return f"Challange: {self.name}"

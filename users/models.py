from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CitizenScientist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(blank=True, default=0)

    def __str__(self) -> str:
        return f"{self.user.last_name}, {self.user.first_name}"


class Scientist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.last_name}, {self.user.first_name}"

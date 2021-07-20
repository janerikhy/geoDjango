from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class CitizenScientist(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    points = models.IntegerField(blank=True, default=0)
    # Should location also be a part of the model?

    def __str__(self) -> str:
        return f"{self.user.username}"


class Scientist(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self) -> str:
        return f"{self.user.username}"

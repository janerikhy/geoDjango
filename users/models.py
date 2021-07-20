from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class CitizenScientist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(blank=True, default=0)
    # Should location also be a part of the model?

    def __str__(self) -> str:
        return f"{self.user.last_name}, {self.user.first_name}"


class Scientist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.last_name}, {self.user.first_name}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CitizenScientist.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print(f"Instance={instance}")
    print(f"Sender={sender}")
    instance.citizenscientist.save()

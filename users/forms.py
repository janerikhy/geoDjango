from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CitizenScientist, Scientist

# The alternative way to create these user views


class CSUserSingUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        cs = CitizenScientist.objects.create(user=user)
        return user


class ScientistSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        sci = Scientist.objects.create(user=user)
        return user

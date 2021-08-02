from django import forms
from django.contrib.admin import widgets

from .models import AreaOfInterest, ObservationTest


class UploadImageForm(forms.ModelForm):

    class Meta:
        model = ObservationTest
        fields = ['image']


class AreaForm(forms.ModelForm):

    class Meta:
        model = AreaOfInterest
        fields = ['name', 'area']
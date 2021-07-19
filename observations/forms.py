from django import forms
from .models import ObservationTest


class UploadImageForm(forms.ModelForm):

    class Meta:
        model = ObservationTest
        fields = ['image']

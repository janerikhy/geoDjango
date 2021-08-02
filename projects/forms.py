from django.forms.widgets import HiddenInput
from users.models import Scientist
from django.contrib.gis import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.core.exceptions import ValidationError
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_time', 'end_time', 'image',
                  'video', 'species', 'areas', 'challenges','organizers', 'environments', 'is_public']
        widgets = {
            'start_time': AdminDateWidget(),
            'end_time': AdminDateWidget(),
            'owner': forms.HiddenInput(),
            'environments': forms.CheckboxSelectMultiple(),
            'organizers': forms.CheckboxSelectMultiple(),
            'challenges': forms.CheckboxSelectMultiple(),
            'species': forms.CheckboxSelectMultiple()
        }



from django import template
import datetime
from django.contrib.gis.geos import Polygon, polygon
from django.core.exceptions import EmptyResultSet
from projects.forms import ProjectForm

register = template.Library()

@register.filter(name="dict_key")
def dict_key(d, k):
    return d.get(k).label.lower()

@register.filter(name="validate")
def validate(error_dict, k):
    print(f"Passed key k:{k}")
    print(f"Error keys: {error_dict.keys()}")
    if k not in error_dict.keys():
        return True
    else:
        return False

@register.filter()
def in_request(post_request, key):
    if key in post_request:
        return True
    else:
        return False

@register.filter()
def form_instance(form, postreq):
    f = ProjectForm(postreq)
    print(postreq)
    print(f"Species current values: {f['species'].value()}")
    print(f"Species Choices: {f['species'].field.queryset.all()}")
    if f.is_valid():
        print(f.cleaned_data)
        return f.cleaned_data
    else:
        return f.fields


@register.filter()
def formfield_value(form, key):
    if form[key].value():
        return form[key].value()
    else:
        return []

@register.filter()
def to_str(val):
    return str(val)
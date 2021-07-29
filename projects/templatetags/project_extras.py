from django import template
import datetime
from django.contrib.gis.geos import Polygon, polygon

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


@register.filter(name="validate_name")
def validate_name(form, name):
    if isinstance(name, str):
        if len(name) < form.fields['name'].max_length:
            return True
    else:
        return False

@register.filter()
def validate_date(form, date):
    print(f"Form: {form}")
    print(date)
    print(f"type: {type(date)}")
    if isinstance(date, datetime.datetime):
        if date >= datetime.datetime.now():
            return True
    else:
        return False

@register.filter()
def validate_polygon(form, figure):
    if isinstance(figure, Polygon):
        return True
    else:
        return False
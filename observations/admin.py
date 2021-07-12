from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis.geos import Point
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import NatureReserve, AreaOfInterest, ObservationTest

# Register your models here.


@admin.register(NatureReserve)
class NatureReserveAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')


@admin.register(AreaOfInterest)
class AreaOfInterest(OSMGeoAdmin):
    list_display = ("name", )


@admin.register(ObservationTest)
class Observation(OSMGeoAdmin):
    fields = ('image', 'user')

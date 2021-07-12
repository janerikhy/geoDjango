from django.contrib import admin
from django.contrib.admin.filters import ChoicesFieldListFilter
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users.models import CitizenScientist, Scientist

# Register your models here.


class CSInline(admin.StackedInline):
    model = CitizenScientist
    can_delete = False
    verbose_name_plural = 'Citizen Scientist'


class ScientistInline(admin.StackedInline):
    model = Scientist
    can_delete = True
    verbose_name_plural = "Scientist"


class UserAdmin(BaseUserAdmin):
    inlines = (CSInline, ScientistInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(CitizenScientist)
admin.site.register(Scientist)

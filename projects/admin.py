from django.contrib import admin
from .models import Species, Project, Environment, Organization, Reward, Sponsor
# Register your models here.


admin.site.register(Species)
admin.site.register(Project)
admin.site.register(Environment)
admin.site.register(Organization)
admin.site.register(Reward)
admin.site.register(Sponsor)
from django import template
from users.models import CitizenScientist

register = template.Library()

@register.filter()
def user_joined(project, user):
    cs = CitizenScientist.objects.get(user=user)
    if project.participants.filter(user=cs).exists():
        return True
    else:
        return False
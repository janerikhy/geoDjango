from users.models import CitizenScientist, Scientist
from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.contrib.auth.decorators import user_passes_test


def cs_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"):
    '''
    Decorator for views that checks that the logged in user is a citizen scientist, redicrects to the log-in page if necessary.
    '''

    actual_decorator = user_passes_test(lambda u: u.is_active and CitizenScientist.objects.filter(user__id=u.id).exists(),
                                        login_url=login_url,
                                        redirect_field_name=redirect_field_name)
    if function:
        return actual_decorator(function)

    return actual_decorator


def researcher_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"):
    '''
    Decorator for views that checks that the logged in user is a researcher, redirects to log-in page if necessary
    '''

    actual_decorator = user_passes_test(lambda u: u.is_active and Scientist.objects.filter(user__id=u.id).exists(),
                                        login_url=login_url,
                                        redirect_field_name=redirect_field_name)

    if function:
        return actual_decorator(function)
    return actual_decorator

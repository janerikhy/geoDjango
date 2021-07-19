from django.urls import path
from django.views.generic.edit import CreateView
from users.views import CreateUserView, register

urlpatterns = [
    path('new_user/create', register, name="new_user"),
]

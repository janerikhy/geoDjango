from django.urls import path
from django.views.generic.edit import CreateView
from users.views import CreateUserView, ProfileView, register

urlpatterns = [
    path('new_user/create', register, name="sign_up"),
    path('profile_<int:pk>', ProfileView.as_view(), name="profile")
]

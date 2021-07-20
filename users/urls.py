from django.urls import path
from users.views import CreateResearcherView, CreateCSUserView, SignUpView

urlpatterns = [
    path('signup', SignUpView.as_view(), name="sign_up"),
    path('new_user/create', CreateCSUserView.as_view(), name="sign_up_cs"),
    path('new_scientist/create', CreateResearcherView.as_view(),
         name="sign_up_researcher")
]

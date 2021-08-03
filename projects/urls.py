from django.urls import path
from .views import ProjectsListView, ProjectDetailView, ProjectCreateView, joinProject


urlpatterns = [
    path('', ProjectsListView.as_view(), name="projects"),
    path('<int:pk>', ProjectDetailView.as_view(), name="project_detail"),
    path('new_project/', ProjectCreateView.as_view(), name="project_create"),
    path('join_<int:pk>', joinProject, name="join")
]

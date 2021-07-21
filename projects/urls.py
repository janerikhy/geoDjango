from django.urls import path
from .views import ProjectsListView, ProjectDetailView, ProjectCreateView


urlpatterns = [
    path('', ProjectsListView.as_view(), name="projects"),
    path('<int:pk>', ProjectDetailView.as_view(), name="project_detail"),
    path('new_project/', ProjectCreateView.as_view(), name="project_create")
]

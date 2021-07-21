from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, DetailView, ListView
from .models import Project
from .forms import ProjectForm
from django.urls import reverse_lazy
from users.decorators import researcher_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


@method_decorator([login_required, researcher_required], name="dispatch")
class ProjectCreateView(CreateView):
    # view for creating new projects
    model = Project
    form_class = ProjectForm
    template_name = "projects/create_project.html"
    success_url = reverse_lazy('projects')


class ProjectsListView(ListView):
    # View for displaying all existing projects, filtered by distance from your location
    model = Project
    template_name = "projects/list_projects.html"


class ProjectDetailView(DetailView):
    # View for a specific project
    model = Project
    template_name = "projects/detail_project.html"

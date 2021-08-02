from observations.models import AreaOfInterest
from typing import Sized
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, DetailView, ListView
from .models import Project
from users.models import Scientist
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
    template_name = "projects/create_proj.html"
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        project = form.save(commit=False)
        print(f"Project: {project}")
        print(f"User: {self.request.user}")
        project.owner = Scientist.objects.filter(user=self.request.user)[0]
        # Create new area from drawn location
        area = AreaOfInterest(name=project.name, area=project.location, scientist=project.owner)
        area.save()
        project.save()
        project.areas.add(area)
        project.save()
        return super(ProjectCreateView, self).form_valid(form)




class ProjectsListView(ListView):
    # View for displaying all existing projects, filtered by distance from your location
    model = Project
    template_name = "projects/list_projects.html"


class ProjectDetailView(DetailView):
    # View for a specific project
    model = Project
    template_name = "projects/detail_project.html"

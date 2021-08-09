from django.http.response import HttpResponseRedirect
from observations.models import AreaOfInterest
from typing import Sized
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, DetailView, ListView
from .models import Project
from users.models import CitizenScientist, Scientist
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.object.areas.first().plot_data()
        context['obs_data'] = self.object.observation_data()
        return context


@login_required
def joinProject(request, pk):
    if request.method == "GET": 
        user = request.user
        if user in [u.user for u in CitizenScientist.objects.all()]:
            print(f"The users: {user}, is a citizen scientist")

            project = get_object_or_404(Project, pk=pk)
            cs = get_object_or_404(CitizenScientist, user=user)
            if not project.participants.filter(user=user).exists():
                project.participants.add(cs)
                print(f"{user} added to {project}")
    else:
        print("METHOD WAS NOT GET")
    
    return HttpResponseRedirect(f'{pk}')
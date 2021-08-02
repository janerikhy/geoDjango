import observations.utils as ML
import geocoder
import os
from django.urls import reverse_lazy
from typing import ContextManager, List
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from iMap.settings import BASE_DIR, GEOCODER_API_KEY
from .models import AreaOfInterest, NatureReserve, ObservationTest
from users.models import CitizenScientist, Scientist
from iMap.settings import MEDIA_ROOT
from .forms import UploadImageForm, AreaForm


# Create your views here.


class HomeView(ListView):
    template_name = "index.html"
    model = AreaOfInterest

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        observations = ObservationTest.objects.all()
        areas = AreaOfInterest.objects.all()
        context['observations'] = observations
        context['areas'] = areas
        context['locations'] = []
        for obs in observations:
            context['locations'].append(geocoder.google(
                [obs.lat, obs.lon], method="reverse", key=GEOCODER_API_KEY))
            #print(os.path.join(BASE_DIR, obs.image.url))
            # print(os.path.abspath(obs.image.url))
            # ML.predict_img(obs.image.path)

        return context


class AOIView(DetailView):
    """
        View to show a specific area of interest and how many observations is registered within it
    """
    template_name = "aoi.html"
    model = AreaOfInterest


class LeaderboardView(ListView):
    model = CitizenScientist
    template_name = "users/leaderboard.html"
    ordering = ["-points"]


@method_decorator(login_required, name="dispatch")
class UploadView(PermissionRequiredMixin, CreateView):
    model = ObservationTest
    form_class = UploadImageForm
    template_name = "observations/upload.html"
    success_url = reverse_lazy('home')
    permission_required = 'observation.can_upload_observation'

    def form_valid(self, form):
        obj = form.save(commit=False)
        print(f"user:  {self.request.user}")
        print(f"user_id: {self.request.user.username}")
        citizen_scientist = CitizenScientist.objects.get(
            user__username=self.request.user.username)
        obj.user = citizen_scientist
        obj.save()
        return super(UploadView, self).form_valid(form)


@method_decorator(login_required, name="dispatch")
class CreateArea(CreateView):
    model = AreaOfInterest
    form_class = AreaForm
    template_name = "observations/create_area.html"
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        scientist = Scientist.objects.get(user=self.request.user)
        obj.scientist = scientist
        obj.save()
        return super(CreateArea, self).form_valid(form)
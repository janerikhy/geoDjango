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
from .utils import predict_img
import json


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
        context['last_observation'] = ObservationTest.objects.all().order_by('-upload_date')[0]
        context['locations'] = []
        for obs in observations:
            context['locations'].append(geocoder.google(
                [obs.lat, obs.lon], method="reverse", key=GEOCODER_API_KEY))
            
        obs_geojson = {
            'type': 'geojson',
            'data': {
                'type': 'FeatureCollection',
                'features': []
            }
        }
        for obs in observations:
            geojson = json.loads(obs.coordinate.geojson)
            obs_date = obs.obs_date.strftime("%b %d %Y %H:%M:%S")
            pk = obs.pk
            u_name = obs.user
            href = f"observation/{u_name}/{pk}"
            src = obs.image.url
            geojson = {
                'type': 'Feature',
                'properties': {
                    'description': "<div class='observation_popup'><div class='lead'>{}</div><a href={}><img class='observation_img' src={}></a></div>".format(
                        obs_date, href, src
                    )
                },
                'geometry': geojson
            }
            obs_geojson['data']['features'].append(geojson)
        context['observation_geojson'] = obs_geojson
        return context


class AOIView(DetailView):
    """
        View to show a specific area of interest and how many observations is registered within it
    """
    template_name = "aoi.html"
    model = AreaOfInterest

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['predictions'] = []
        observations = self.object.observations.all()
        for obs in observations:
            _, prediction_dict = predict_img(obs.image.path)
            context['predictions'].append(prediction_dict)
        return context


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
    permission_required = 'observations.can_upload_observation'

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

class ObservationDetailView(DetailView):
    model = ObservationTest
    template_name = "observations/observation_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _, context['prediction'] = predict_img(self.object.image.path)
        return context


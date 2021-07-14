import observations.utils as ML
import geocoder
import os
from typing import ContextManager, List
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.utils.safestring import SafeString
from iMap.settings import BASE_DIR, GEOCODER_API_KEY
from .models import AreaOfInterest, NatureReserve, ObservationTest
from users.models import CitizenScientist
from iMap.settings import MEDIA_ROOT


# Create your views here.


class HomeView(ListView):
    template_name = "index.html"
    model = AreaOfInterest
    print(MEDIA_ROOT)

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
            print(os.path.join(BASE_DIR, obs.image.url))
            print(os.path.abspath(obs.image.url))
            ML.predict_img(obs.image.path)

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

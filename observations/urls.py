from django.urls import path
from .views import HomeView, AOIView, LeaderboardView, ObservationDetailView, UploadView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("area-of-interest-<int:pk>", AOIView.as_view(), name="aoi"),
    path("leaderboard", LeaderboardView.as_view(), name="leaderboard"),
    path("upload", UploadView.as_view(), name="upload"),
    path("observation/<str:username>/<int:pk>",
         ObservationDetailView.as_view(), name="obs_detail")
]

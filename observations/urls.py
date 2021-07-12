from django.urls import path
from .views import HomeView, AOIView, LeaderboardView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("area-of-interest-<int:pk>", AOIView.as_view(), name="aoi"),
    path("leaderboard", LeaderboardView.as_view(), name="leaderboard")
]

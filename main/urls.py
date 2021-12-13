from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("", views.IndexView, name="index"),

	path("banner/", views.BannerView, name="banner"),

	path("unvetted/", views.UnvettedView, name="unvetted"),



	#coin urls
	path("chart/zoom-swap/", views.ZoomSwapView, name="zoom_swap"),
	path("chart/vitality/", views.VitalityView, name="vitality"),
	path("chart/game-fantasy-token/", views.GameFantasyTokenView, name="game_fantasy_token"),

	
	
]
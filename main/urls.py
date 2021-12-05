from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("", views.IndexView, name="index"),

	path("banner/", views.BannerView, name="banner"),

	path("unvetted/", views.UnvettedView, name="unvetted"),
]
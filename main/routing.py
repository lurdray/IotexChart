from django.urls import path
from .consumer import Consumer

ws_urlpatterns = [
	
	path("ws-connect/", Consumer.as_asgi())
]
from django.db import models
from django.utils import timezone

# Create your models here.


class ZoomSwap(models.Model):
	price = models.CharField(max_length=500, default="Crypto Data")
	date = models.CharField(max_length=500, default="Crypto Data")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.price





class Vitality(models.Model):
	price = models.CharField(max_length=500, default="Crypto Data")
	date = models.CharField(max_length=500, default="Crypto Data")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.price




class GameFantasyToken(models.Model):
	price = models.CharField(max_length=500, default="Crypto Data")
	date = models.CharField(max_length=500, default="Crypto Data")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.price
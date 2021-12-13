from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


from datetime import datetime
import requests
import time
from datetime import datetime, timedelta
from django.utils import timezone

from .models import *



def UpdateZoomSwap(new_data):

	for item in new_data:
		new_crypto_data = ZoomSwap.objects.create(price=item[1], date=item[0])
		new_crypto_data.save()


def UpdateVitality(new_data):

	for item in new_data:
		new_crypto_data = Vitality.objects.create(price=item[1], date=item[0])
		new_crypto_data.save()


def UpdateGameFantasyToken(new_data):

	for item in new_data:
		new_crypto_data = GameFantasyToken.objects.create(price=item[1], date=item[0])
		new_crypto_data.save()




def IndexView(request):
	if request.method == "POST":
		pass


	else:

		context = {}
		return render(request, "main/index.html", context )



def RealTime(request):
	rt_data = []

	pass





def BannerView(request):
	if request.method == "POST":
		pass

	else:
		context = {}
		return render(request, "main/banner.html", context )

def UnvettedView(request):
	if request.method == "POST":
		pass

	else:
		context = {}
		return render(request, "main/unvetted.html", context )







#coin views
def ZoomSwapView(request):
	if request.method == "POST":
		pass


	else:


		crypto_data = ZoomSwap.objects.order_by("-date")

		if len(crypto_data) > 0:
		
			most_recent = crypto_data[0]

			most_recent_date = most_recent.date
			current_date = (timezone.now()).date()
			current_date = new_date = datetime.strptime(str(current_date), "%Y-%m-%d").strftime("%m/%d/%Y")

			sum_most_recent_date = 0
			most_recent_date = most_recent_date.split("/")
			for item in most_recent_date:
				sum_most_recent_date += int(item)

			sum_current_date = 0
			current_date = current_date.split("/")
			for item in current_date:
				sum_current_date += int(item)


			#print(most_recent.date)

			#print("sum_current_date: %s ============= sum_most_recent_date: %s" % (sum_current_date, sum_most_recent_date))

			if sum_most_recent_date == sum_current_date:
				pass

			elif sum_most_recent_date < sum_current_date:
				all_data30 = []

				current_date = (datetime.now()).date()

				for item in range(sum_current_date-sum_most_recent_date):
					new_list = []

					new_date = (current_date-timedelta(days=item))
					new_date = datetime.strptime(str(new_date), "%Y-%m-%d").strftime("%d-%m-%Y")

					response = requests.get("https://api.coingecko.com/api/v3/coins/zoomswap/history?date=%s&localization=false" % (new_date)).json()
					price = response["market_data"]["current_price"]["usd"]

					new_date = datetime.strptime(str(new_date), "%d-%m-%Y").strftime("%m/%d/%Y")
					new_list.append(new_date)
					new_list.append(price)

					all_data30.append(new_list)

					

				UpdateZoomSwap(all_data30)

			else:
				pass

		else:
			
			current_date = (timezone.now()).date()
			current_date = new_date = datetime.strptime(str(current_date), "%Y-%m-%d").strftime("%m/%d/%Y")

			sum_current_date = 0
			current_date = current_date.split("/")
			for item in current_date:
				sum_current_date += int(item)

			sum_most_recent_date = sum_current_date - 30

			if sum_most_recent_date == sum_current_date or sum_most_recent_date < sum_current_date:
				all_data30 = []

				current_date = (datetime.now()).date()

				for item in range(sum_current_date-sum_most_recent_date):
					new_list = []

					new_date = (current_date-timedelta(days=item))
					new_date = datetime.strptime(str(new_date), "%Y-%m-%d").strftime("%d-%m-%Y")

					response = requests.get("https://api.coingecko.com/api/v3/coins/zoomswap/history?date=%s&localization=false" % (new_date)).json()
					price = response["market_data"]["current_price"]["usd"]

					new_date = datetime.strptime(str(new_date), "%d-%m-%Y").strftime("%m/%d/%Y")
					new_list.append(new_date)
					new_list.append(price)

					all_data30.append(new_list)

					

				UpdateZoomSwap(all_data30)


		crypto_data = ZoomSwap.objects.order_by("date")
		

		coin_name = "Zoom Swap"
		context = {"all_data30": crypto_data, "coin_name": coin_name}
		return render(request, "main/live_chart.html", context )





def VitalityView(request):
	if request.method == "POST":
		pass


	else:


		crypto_data = Vitality.objects.order_by("-date")

		if len(crypto_data) > 0:
		
			most_recent = crypto_data[0]

			most_recent_date = most_recent.date
			current_date = (timezone.now()).date()
			current_date = new_date = datetime.strptime(str(current_date), "%Y-%m-%d").strftime("%m/%d/%Y")

			sum_most_recent_date = 0
			most_recent_date = most_recent_date.split("/")
			for item in most_recent_date:
				sum_most_recent_date += int(item)

			sum_current_date = 0
			current_date = current_date.split("/")
			for item in current_date:
				sum_current_date += int(item)


			#print(most_recent.date)

			#print("sum_current_date: %s ============= sum_most_recent_date: %s" % (sum_current_date, sum_most_recent_date))

			if sum_most_recent_date == sum_current_date:
				pass

			elif sum_most_recent_date < sum_current_date:
				all_data30 = []

				current_date = (datetime.now()).date()

				for item in range(sum_current_date-sum_most_recent_date):
					new_list = []

					new_date = (current_date-timedelta(days=item))
					new_date = datetime.strptime(str(new_date), "%Y-%m-%d").strftime("%d-%m-%Y")

					response = requests.get("https://api.coingecko.com/api/v3/coins/vitality/history?date=%s&localization=false" % (new_date)).json()
					price = response["market_data"]["current_price"]["usd"]

					new_date = datetime.strptime(str(new_date), "%d-%m-%Y").strftime("%m/%d/%Y")
					new_list.append(new_date)
					new_list.append(price)

					all_data30.append(new_list)

					

				UpdateVitality(all_data30)

			else:
				pass

		else:
			
			current_date = (timezone.now()).date()
			current_date = new_date = datetime.strptime(str(current_date), "%Y-%m-%d").strftime("%m/%d/%Y")

			sum_current_date = 0
			current_date = current_date.split("/")
			for item in current_date:
				sum_current_date += int(item)

			sum_most_recent_date = sum_current_date - 30

			if sum_most_recent_date == sum_current_date or sum_most_recent_date < sum_current_date:
				all_data30 = []

				current_date = (datetime.now()).date()

				for item in range(sum_current_date-sum_most_recent_date):
					new_list = []

					new_date = (current_date-timedelta(days=item))
					new_date = datetime.strptime(str(new_date), "%Y-%m-%d").strftime("%d-%m-%Y")

					response = requests.get("https://api.coingecko.com/api/v3/coins/vitality/history?date=%s&localization=false" % (new_date)).json()
					price = response["market_data"]["current_price"]["usd"]

					new_date = datetime.strptime(str(new_date), "%d-%m-%Y").strftime("%m/%d/%Y")
					new_list.append(new_date)
					new_list.append(price)

					all_data30.append(new_list)

					

				UpdateVitality(all_data30)


		crypto_data = Vitality.objects.order_by("date")
		
		coin_name = "Vitality"
		context = {"all_data30": crypto_data, "coin_name": coin_name}
		return render(request, "main/live_chart.html", context )




def GameFantasyTokenView(request):
	if request.method == "POST":
		pass


	else:


		crypto_data = GameFantasyToken.objects.order_by("-date")

		if len(crypto_data) > 0:
		
			most_recent = crypto_data[0]

			most_recent_date = most_recent.date
			current_date = (timezone.now()).date()
			current_date = new_date = datetime.strptime(str(current_date), "%Y-%m-%d").strftime("%m/%d/%Y")

			sum_most_recent_date = 0
			most_recent_date = most_recent_date.split("/")
			for item in most_recent_date:
				sum_most_recent_date += int(item)

			sum_current_date = 0
			current_date = current_date.split("/")
			for item in current_date:
				sum_current_date += int(item)


			#print(most_recent.date)

			#print("sum_current_date: %s ============= sum_most_recent_date: %s" % (sum_current_date, sum_most_recent_date))

			if sum_most_recent_date == sum_current_date:
				pass

			elif sum_most_recent_date < sum_current_date:
				all_data30 = []

				current_date = (datetime.now()).date()

				for item in range(sum_current_date-sum_most_recent_date):
					new_list = []

					new_date = (current_date-timedelta(days=item))
					new_date = datetime.strptime(str(new_date), "%Y-%m-%d").strftime("%d-%m-%Y")

					response = requests.get("https://api.coingecko.com/api/v3/coins/game-fantasy-token/history?date=%s&localization=false" % (new_date)).json()
					price = response["market_data"]["current_price"]["usd"]

					new_date = datetime.strptime(str(new_date), "%d-%m-%Y").strftime("%m/%d/%Y")
					new_list.append(new_date)
					new_list.append(price)

					all_data30.append(new_list)

					

				UpdateGameFantasyToken(all_data30)

			else:
				pass

		else:
			
			current_date = (timezone.now()).date()
			current_date = new_date = datetime.strptime(str(current_date), "%Y-%m-%d").strftime("%m/%d/%Y")

			sum_current_date = 0
			current_date = current_date.split("/")
			for item in current_date:
				sum_current_date += int(item)

			sum_most_recent_date = sum_current_date - 30

			if sum_most_recent_date == sum_current_date or sum_most_recent_date < sum_current_date:
				all_data30 = []

				current_date = (datetime.now()).date()

				for item in range(sum_current_date-sum_most_recent_date):
					new_list = []

					new_date = (current_date-timedelta(days=item))
					new_date = datetime.strptime(str(new_date), "%Y-%m-%d").strftime("%d-%m-%Y")

					response = requests.get("https://api.coingecko.com/api/v3/coins/game-fantasy-token/history?date=%s&localization=false" % (new_date)).json()
					price = response["market_data"]["current_price"]["usd"]

					new_date = datetime.strptime(str(new_date), "%d-%m-%Y").strftime("%m/%d/%Y")
					new_list.append(new_date)
					new_list.append(price)

					all_data30.append(new_list)

					

				UpdateGameFantasyToken(all_data30)


		crypto_data = GameFantasyToken.objects.order_by("date")
		

		coin_name = "Game Fantasy Token"
		context = {"all_data30": crypto_data, "coin_name": coin_name}
		return render(request, "main/live_chart.html", context )

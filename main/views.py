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



def GetData():
	apiUrl = "https://api.pro.coinbase.com"
	sym = "IOTX-USD"
	barSize = "60"

	timeEnd = datetime.now()
	delta = timedelta(seconds=int(barSize))

	timeStart = timeEnd - (1*delta)

	timeStart = timeStart.isoformat()
	timeEnd = timeEnd.isoformat()

	parameters = {
		"start": timeStart,
		"end": timeEnd,
		"granularity": "60",
	}
	headers = {"content-type": "application/json"}

	data = requests.get(f"{apiUrl}/products/{sym}/candles",
			params=parameters,
			headers=headers).json()

	return data



def IndexView(request):
	if request.method == "POST":
		pass


	else:

		#1day chart
		response = requests.get("https://api.coingecko.com/api/v3/coins/iotex/ohlc?vs_currency=usd&days=1").json()
		#data = GetData()
		data1 = []

		for item in response:
			new_list = []
			new_list.append(item[0])
			new_list.append(item[1])
			new_list.append(item[2])
			new_list.append(item[3])
			new_list.append(item[4])

			data1.append(new_list)


		#1day chart
		response = requests.get("https://api.coingecko.com/api/v3/coins/iotex/ohlc?vs_currency=usd&days=7").json()
		#data = GetData()
		data7 = []

		for item in response:
			new_list = []
			new_list.append(item[0])
			new_list.append(item[1])
			new_list.append(item[2])
			new_list.append(item[3])
			new_list.append(item[4])

			data7.append(new_list)

		#1day chart
		response = requests.get("https://api.coingecko.com/api/v3/coins/iotex/ohlc?vs_currency=usd&days=14").json()
		#data = GetData()
		data14 = []

		for item in response:
			new_list = []
			new_list.append(item[0])
			new_list.append(item[1])
			new_list.append(item[2])
			new_list.append(item[3])
			new_list.append(item[4])

			data14.append(new_list)

		#1day chart
		response = requests.get("https://api.coingecko.com/api/v3/coins/iotex/ohlc?vs_currency=usd&days=30").json()
		#data = GetData()
		data30 = []

		for item in response:
			new_list = []
			new_list.append(item[0])
			new_list.append(item[1])
			new_list.append(item[2])
			new_list.append(item[3])
			new_list.append(item[4])

			data30.append(new_list)

		#1day chart
		response = requests.get("https://api.coingecko.com/api/v3/coins/iotex/ohlc?vs_currency=usd&days=90").json()
		#data = GetData()
		data90 = []

		for item in response:
			new_list = []
			new_list.append(item[0])
			new_list.append(item[1])
			new_list.append(item[2])
			new_list.append(item[3])
			new_list.append(item[4])

			data90.append(new_list)


		#1day chart
		response = requests.get("https://api.coingecko.com/api/v3/coins/iotex/ohlc?vs_currency=usd&days=180").json()
		#data = GetData()
		data180 = []

		for item in response:
			new_list = []
			new_list.append(item[0])
			new_list.append(item[1])
			new_list.append(item[2])
			new_list.append(item[3])
			new_list.append(item[4])

			data180.append(new_list)

		#1day chart
		response = requests.get("https://api.coingecko.com/api/v3/coins/iotex/ohlc?vs_currency=usd&days=365").json()
		#data = GetData()
		data365 = []

		for item in response:
			new_list = []
			new_list.append(item[0])
			new_list.append(item[1])
			new_list.append(item[2])
			new_list.append(item[3])
			new_list.append(item[4])

			data365.append(new_list)

		context = {"data1": data1, "data7": data7, "data14": data14, "data30": data30, "data90": data90, "data180": data180, "data365": data365}
		return render(request, "main/index.html", context )


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
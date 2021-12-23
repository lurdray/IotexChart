from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required




from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests

#from .forms import UserForm

from datetime import datetime
from requests import Request, Session
import json
import time
from datetime import datetime, timedelta

from bs4 import BeautifulSoup
from selenium import webdriver


#data = requests.get("https://iotexscan.io/token/0xe2F300065C1ebfc2BE8574da8063dd0721C85A33")
#soup = BeautifulSoup(data.content, 'html5lib')

#driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver") 
#driver.get("https://iotexscan.io/token/0xe2F300065C1ebfc2BE8574da8063dd0721C85A33")

#html = driver.execute_script("return document.documentElement.innerHTML")
#new_soup = BeautifulSoup(html, "html.parser")

#data = new_soup.find_all('p', class_='chakra-text')
#price = data[0].get_text()

#print(data)
print("####################################################")

def NoneView(request):
	if request.method == "POST":
		pass

	else:

		banner = Banner.objects.all().order_by('-pub_date')[:4]
		
		#side_banner = Banner.objects.all().order_by('-pub_date')[1:3]
		aside_banner = Banner.objects.all().order_by('-pub_date')[1:3]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=game-fantasy-token&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		vita = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=vitality&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		zoom = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=zoomswap&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		iotex = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=iotex&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		metanyx = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=metanyx&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		iotexshiba = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=iotexshiba&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		imagictoken = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=imagictoken&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		wow = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=wowswap&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		
		context = {"banner": banner,  "aside_banner":aside_banner, "data":data, "vita":vita, "zoom":zoom, "iotex":iotex, "metanyx":metanyx, "iotexshiba":iotexshiba, "imagictoken":imagictoken, "wow":wow}
		
		time.sleep(6)
		return render(request, "main/none.html", context)



def IotexChartView(request):
	if request.method == "POST":
		pass
	else:
		data = IotexChart.objects.order_by("pub_date")

		prices = [item.price for item in data]

		ath = max(prices)
		atl = min(prices)
		price = prices[-1]

		context = {"data":data, "ath": ath, "atl": atl,"price": price}

		#time.sleep(6)
		return render(request, "main/iotexchart.html", context)



def WowSwapView(request):
	if request.method == "POST":
		pass
	else:
		response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=wowswap&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
		image = Banner.objects.all().order_by('?')[:1]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=wowswap&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		price = str(response["wowswap"]["usd"])
		market_cap = int(response["wowswap"]["usd_market_cap"])
		hr_vol = str(response["wowswap"]["usd_24h_vol"])
		hr_chg = str(response["wowswap"]["usd_24h_change"])
		last_updated = str(response["wowswap"]["last_updated_at"])
		context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated, "image":image}
		
		time.sleep(6)
		return render(request, "main/wow.html", context)


def ImagicTokenView(request):
	if request.method == "POST":
		pass
	else:
		response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=imagictoken&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
		image = Banner.objects.all().order_by('?')[:1]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=imagictoken&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		price = str(response["imagictoken"]["usd"])
		market_cap = int(response["imagictoken"]["usd_market_cap"])
		hr_vol = str(response["imagictoken"]["usd_24h_vol"])
		hr_chg = str(response["imagictoken"]["usd_24h_change"])
		last_updated = str(response["imagictoken"]["last_updated_at"])
		context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated, "image":image}
		
		time.sleep(6)
		return render(request, "main/imagictoken.html", context)


def IotexShibaView(request):
	if request.method == "POST":
		pass
	else:
		response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=iotexshiba&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
		image = Banner.objects.all().order_by('?')[:1]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=iotexshiba&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		price = str(response["iotexshiba"]["usd"])
		market_cap = int(response["iotexshiba"]["usd_market_cap"])
		hr_vol = str(response["iotexshiba"]["usd_24h_vol"])
		hr_chg = str(response["iotexshiba"]["usd_24h_change"])
		last_updated = str(response["iotexshiba"]["last_updated_at"])
		context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated, "image":image}
		
		time.sleep(6)
		return render(request, "main/iotexshiba.html", context)


def MetanyxView(request):
	if request.method == "POST":
		pass
	else:
		response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=metanyx&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
		image = Banner.objects.all().order_by('?')[:1]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=metanyx&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		price = str(response["metanyx"]["usd"])
		market_cap = int(response["metanyx"]["usd_market_cap"])
		hr_vol = str(response["metanyx"]["usd_24h_vol"])
		hr_chg = str(response["metanyx"]["usd_24h_change"])
		last_updated = str(response["metanyx"]["last_updated_at"])
		context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated, "image":image}
		
		time.sleep(6)
		return render(request, "main/metanyx.html", context)

def IotexView(request):
	if request.method == "POST":
		pass
	else:
		response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=iotex&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
		image = Banner.objects.all().order_by('?')[:1]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=iotex&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		price = str(response["iotex"]["usd"])
		market_cap = int(response["iotex"]["usd_market_cap"])
		hr_vol = str(response["iotex"]["usd_24h_vol"])
		hr_chg = str(response["iotex"]["usd_24h_change"])
		last_updated = str(response["iotex"]["last_updated_at"])
		context = {"image":image, "data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated}
		
		time.sleep(6)
		return render(request, "main/iotex.html", context)



def ZoomSwapView(request):
	if request.method == "POST":
		pass
	else:
		response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=zoomswap&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
		image = Banner.objects.all().order_by('?')[:1]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=zoomswap&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		price = str(response["zoomswap"]["usd"])
		market_cap = int(response["zoomswap"]["usd_market_cap"])
		hr_vol = str(response["zoomswap"]["usd_24h_vol"])
		hr_chg = str(response["zoomswap"]["usd_24h_change"])
		last_updated = str(response["zoomswap"]["last_updated_at"])
		context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated, "image":image}
		
		time.sleep(6)
		return render(request, "main/zoomswap.html", context)

def GameFantasyTokenView(request):
	if request.method == "POST":
		pass
	else:
		response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=game-fantasy-token&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
		image = Banner.objects.all().order_by('?')[:1]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=game-fantasy-token&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		price = str(response["game-fantasy-token"]["usd"])
		market_cap = int(response["game-fantasy-token"]["usd_market_cap"])
		hr_vol = str(response["game-fantasy-token"]["usd_24h_vol"])
		hr_chg = str(response["game-fantasy-token"]["usd_24h_change"])
		last_updated = str(response["game-fantasy-token"]["last_updated_at"])
		
		context = {"image":image, "data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated}
		
		time.sleep(6)
		return render(request, "main/gamefantasy.html", context)

def VitalityView(request):
	if request.method == "POST":
		pass
	else:
		response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=vitality&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
		image = Banner.objects.all().order_by('?')[:1]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=vitality&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		price = str(response["vitality"]["usd"])
		market_cap = int(response["vitality"]["usd_market_cap"])
		hr_vol = str(response["vitality"]["usd_24h_vol"])
		hr_chg = str(response["vitality"]["usd_24h_change"])
		last_updated = str(response["vitality"]["last_updated_at"])
		context = {"image":image, "data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated}
		
		time.sleep(6)
		return render(request, "main/vitality.html", context)



def GetUrlViaAddress(address):

	if address == "io1secz5lugnzch9h3ed6esf47czgr3y7g43k5jcv":
		url = "zoom_swap"
	
	elif address == "io1hp6y4eqr90j7tmul4w2wa8pm7wx462hq0mg4tw":
		url = "vitality"

	elif address == "io16e77pc9ql4a3thyrfzaehe6z70zc2pz5x60q22":
		url = "wow"

	elif address == "io1zl0el07pek4sly8dmscccnm0etd8xr8j02t4y7":
		url = "game_fantasy_token"

	elif address == "io1gafy2msqmmmqyhrhk4dg3ghc59cplyhekyyu26":
		url = "metanyx"

	elif address == "io186ngxd2tlrf4nnv7cmsgkkhv9ywhrkyq8rejue":
		url = "iotex_shiba"

	elif address == "io1fyx0h7decsmr8hw3j6xsv2vkyfl0gw9fcz3hfz":
		url = "imagictoken"

	else:
		url = "iotex"


	return url



def GetUrlViaName(name):

	if name == "ZoomSwap (zm)":
		url = "zoom_swap"
	
	elif name == "Vitality (vita)":
		url = "vitality"

	elif name == "WOWswap (wow)":
		url = "wow"

	elif name == "Game Fantasy Token (gft)":
		url = "game_fantasy_token"

	elif name == "Metanyx (metx)":
		url = "metanyx"

	elif name == "IoTexShiba (ioshib)":
		url = "iotex_shiba"

	elif name == "iMagicToken (imagic)":
		url = "imagictoken"

	else:
		url = "iotex"


	return url



def IndexView(request):
	if request.method == "POST":

		address_db = ["io1secz5lugnzch9h3ed6esf47czgr3y7g43k5jcv", "io1hp6y4eqr90j7tmul4w2wa8pm7wx462hq0mg4tw",
		"io16e77pc9ql4a3thyrfzaehe6z70zc2pz5x60q22", "io1zl0el07pek4sly8dmscccnm0etd8xr8j02t4y7",
		"io1gafy2msqmmmqyhrhk4dg3ghc59cplyhekyyu26", "io186ngxd2tlrf4nnv7cmsgkkhv9ywhrkyq8rejue",
		"io1fyx0h7decsmr8hw3j6xsv2vkyfl0gw9fcz3hfz"]

		name_db = ["ZoomSwap (zm)", "Vitality (vita)", "WOWswap (wow)", "Game Fantasy Token (gft)",
		"Metanyx (metx)", "IoTexShiba (ioshib)", "iMagicToken (imagic)"]
		
		status = False
		result = None
		url = "none"

		query = request.POST.get("query")


		for item in address_db:
			if query == item:
				result = item

				url = GetUrlViaAddress(result)


		for item in name_db:
			if query in item:
				result = item

				url = GetUrlViaName(result)

		time.sleep(6)
		return HttpResponseRedirect(reverse("main:%s" % (url)))




	else:
		banner = Banner.objects.all().order_by('-pub_date')[:4]
		
		side_banner = Banner.objects.all().order_by('-pub_date')[1:3]
		aside_banner = Banner.objects.all().order_by('-pub_date')[1:3]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=game-fantasy-token&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		vita = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=vitality&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		zoom = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=zoomswap&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		iotex = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=iotex&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		metanyx = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=metanyx&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		iotexshiba = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=iotexshiba&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		imagictoken = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=imagictoken&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		wow = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=wowswap&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		
		time.sleep(6)
		context = {"banner": banner, "side_banner":side_banner, "aside_banner":aside_banner, "data":data, "vita":vita, "zoom":zoom, "iotex":iotex, "metanyx":metanyx, "iotexshiba":iotexshiba, "imagictoken":imagictoken, "wow":wow}
		return render(request, "main/index.html", context )

@login_required(login_url='/signin')
def AllBannerView(request):

	#url = "https://iotexscan.io/api/getInitData"

	#payload={}
	#headers = {}

	#response = requests.request("GET", url, headers=headers, data=payload)
	banner = Banner.objects.all().order_by('-pub_date')


	context = {
		
		"banner": banner,
		#"response":response,

		}

	return render(request, "main/allbanner.html", context )

@login_required(login_url='/signin')
def VerifyBannerView(request, pk):
	banner = Banner.objects.get(id=pk)
	context = {
		"banner":banner
	}
	#form = VerifyBannerForm(request.POST or None)
	if request.method == "POST":
		banner = Banner.objects.get(id=pk)
		banner.status = True
		banner.save()
			
		messages.success(request, 'updated')
		#return HttpResponseRedirect(reverse("main:verify_banner"))
		#return redirect(reverse('verify_banner'))

	else:
		pass

	return render(request, 'main/verify_banner.html', context)


def BannerView(request):
	form = BannerForm(request.POST, request.FILES)
	context = {'form': form}
	if request.method == "POST":
		if form.is_valid():
			title = form.cleaned_data.get('title')
			text = form.cleaned_data.get('text')
			link = form.cleaned_data.get('link')
			company_name = form.cleaned_data.get('company_name')
			image = request.FILES['image']
			interest = form.cleaned_data.get('interest')
			budget = form.cleaned_data.get('budget')
			proof_of_payment = form.cleaned_data.get('proof_of_payment')
			about_project = form.cleaned_data.get('about_project')

			try:
				form = Banner()
				form.title = title
				form.text  = text 
				form.link = link
				form.company_name = company_name
				form.image = image
				form.interest = interest
				form.budget = budget
				form.proof_of_payment = proof_of_payment
				form.about_project = about_project
				form.save()
				messages.success(request, "Submitted Successfully")
				return render(request, "main/banner.html", context)
			except Exception as e:
				messages.error(request, 'Could Not Add ' + str(e))

		else:
			messages.error(request, 'Fill Form Properly ')
	return render(request, "main/banner.html", context )

def unvetted(request):
	form = UnvettedForm(request.POST, request.FILES)
	context = {'form': form}
	if request.method == 'POST':
		if form.is_valid():
			token_address = form.cleaned_data.get('token_address')
			telegram_url = form.cleaned_data.get('telegram_url')
			#proof_of_payment = form.cleaned_data.get("proof_of_payment")
			image = request.FILES['image']

			try:
				form = Unvetted()
				form.token_address = token_address
				form.telegram_url = telegram_url
				#proof_of_payment = proof_of_payment
				form.image = image
				form.save()
				messages.success(request, "Submitted Successfully")
				return render(request, "main/unvetted.html", context)

			except Exception as e:
				messages.error(request, 'Could Not Add ' + str(e))

		else:
			messages.error(request, 'Fill Form Properly ')

	return render(request, "main/unvetted.html", context)
@login_required(login_url='/signin')
def AllVettedView(request):
	vetted = Unvetted.objects.all().order_by('-pub_date')

	context = {	
		"vetted": vetted,
		}

	return render(request, "main/allvetted.html", context )

@login_required(login_url='/signin')
def VerifyVettedView(request, pk):
	vetted = Unvetted.objects.get(id=pk)

		

	context = {
		"vetted":vetted, 

		}
	if request.method == "POST":
		vetted = Unvetted.objects.get(id=pk)
		vetted.status = True
		vetted.save()
			
		messages.success(request, 'updated')

	else:
		pass

	return render(request, 'main/verify_vetted.html', context)


def signin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "welcome onboard "+user.username)
			current_user = request.user
			#userprofile = UserProfile.objects.get(user_id = current_user.id)
			#request.session['userimage'] = userprofile.image.url
			return HttpResponseRedirect('/')
		else:
			messages.warning(request, "Login Error !! username or password is incorrect")
			return HttpResponseRedirect('/signin')
	current_user = request.user

	context = {
	}
	return render(request, 'main/signin.html', context)


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()

			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			email = form.cleaned_data.get('email')
			phone = form.cleaned_data.get('phone')
			user = authenticate(username=username, password=password)
			
			login(request, user)
			current_user = request.user
			#data = UserProfile()
			data.user_id = current_user.id
			
			data.image="images.png"
			data.save()
			messages.success(request, 'Account successfully created')
			return HttpResponseRedirect('/')
		else:
			messages.warning(request, form.errors)
			return HttpResponseRedirect('/signup')
	form = SignUpForm()

	context = {'form':form,  }
	return render(request, 'main/signup.html', context)

def logout_func(request):
	logout(request)
	messages.success(request, 'Logged out')
	return HttpResponseRedirect('/')
	
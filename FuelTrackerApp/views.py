from datetime import date, datetime
from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from FuelTrackerApp.forms import FuelStationForm, ReceiptForm, UserForm, VehicleForm
from .models import FuelStation, Receipt, Vehicle


"""VIEWS"""

# INDEX VIEWS
def eco_index(request):
	context = {}
	return render(request, 'FuelTrackerApp/index.html', context)

# HELP VIEWS
def help_index(request):
	return render(request, 'FuelTrackerApp/help/index.html')

# AUTH VIEWS
def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('eco_index')
		else:
			return redirect(request, 'user_login')
	return render(request, 'FuelTrackerApp/auth/login.html')
def user_signup(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		print(form)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			print(new_user)
			login(request, new_user)
			return redirect('eco_index')
	else:
		form = UserForm()
		print(form)
		context = {
			'form': form
		}
		return render(request, 'FuelTrackerApp/auth/signup.html', context)
def user_logout(request):
	if request.method == 'GET':
		logout(request)
	return redirect('eco_index')

# FUEL STATION VIEWS
def fuel_station_index(request):
	try:
		fuel_stations = FuelStation.objects.all()
	except:
		fuel_stations = None
	context = {
		'fuel_stations': fuel_stations
	}
	return render(request, 'FuelTrackerApp/fuel_station/index.html', context)
def fuel_station_detail(request, fuel_station_id):
	fuel_station = get_object_or_404(FuelStation, pk=fuel_station_id)
	context = {
		'fuel_station': fuel_station
	}
	return render(request, 'FuelTrackerApp/fuel_station/detail.html', context)
def fuel_station_new(request):
	if request.method == 'POST':
		form = FuelStationForm(request.POST)
		if form.is_valid():
			next_url = request.POST.get('next')
			model_instance = form.save(commit=False)
			model_instance.timestamp = timezone.now()
			model_instance.save()
			redirect_url = next_url + str(model_instance.id)
			return redirect(redirect_url)
	else:
		form = FuelStationForm()
		context = {
			'form': form
		}
		return render(request, 'FuelTrackerApp/fuel_station/new.html', context)

# RECEIPT VIEWS
def receipt_index(request):
	try:
		# FIXME -- could use prefetch_related() to query vehicles
		vehicles = Vehicle.objects.filter(owner_id=request.user.id)
		print(vehicles)
		receipts = Receipt.objects.filter(vehicle__owner_id=request.user.id)
		print(receipts)
	except:
		receipts = None
	context = {
		'receipts': receipts
	}
	return render(request, 'FuelTrackerApp/receipt/index.html', context)
def receipt_detail(request, receipt_id):
	try:
		print('Searching for Receipt object with pk=' + str(receipt_id))
		receipt = Receipt.objects.get(pk=receipt_id)
		print(receipt)
		print('Searching for FuelStation object with pk=' + str(receipt.gas_station_id))
		fuel_station = FuelStation.objects.get(pk=receipt.gas_station_id)
		print('Searching for Vehicle object with pk=' + str(receipt.vehicle_id))
		vehicle = Vehicle.objects.get(pk=receipt.vehicle_id)
	except:
		raise Http404('Indicated purchase does not exist')
	context = {
		'fuel_station': fuel_station,
		'price_total': round((receipt.price_per_gal * receipt.gallons), 2),
		'receipt': receipt,
		'vehicle': vehicle
	}
	return render(request, 'FuelTrackerApp/receipt/detail.html', context)
def receipt_new(request):
	if request.method == 'POST':
		form = ReceiptForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.timestamp = timezone.now()
			model_instance.save()
			return redirect('receipt_index')
	else:
		vehicles = Vehicle.objects.filter(owner_id=request.user.id)
		fuel_stations = FuelStation.objects.all()
		form = ReceiptForm()
		context = {
			'form': form,
			'fuel_stations': fuel_stations,
			'vehicles': vehicles
		}
		return render(request, 'FuelTrackerApp/receipt/new.html', context)

# VEHICLE VIEWS
def vehicle_index(request):
	try:
		vehicles = Vehicle.objects.filter(owner_id=request.user.id)
	except:
		vehicles = None
	context = {
		'vehicles': vehicles
	}
	return render(request, 'FuelTrackerApp/vehicle/index.html', context)
def vehicle_detail(request, vehicle_id):
	try:
		vehicle = Vehicle.objects.get(pk=vehicle_id)
		receipts =  Receipt.objects.filter(vehicle_id=vehicle.id)
		print(receipts)
		vehicle_stats = {}
		receipts_aggregate = {
			'mi': 0,
			'gal': 0
		}
		for receipt in receipts:
			receipts_aggregate['mi'] += receipt.mi_since_last
			receipts_aggregate['gal'] += receipt.gallons
		vehicle_stats['fuel_economy_overall'] = round(receipts_aggregate['mi'] / receipts_aggregate['gal'], 1)
		vehicle_stats['receipts_no'] = len(receipts)
	except:
		raise Http404('Indicated vehicle does not exist')
	context = {
		'vehicle_stats': vehicle_stats,
		'receipts': receipts,
		'vehicle': vehicle
	}
	return render(request, 'FuelTrackerApp/vehicle/detail.html', context)
def vehicle_new(request):
	try:
		vehicles = Vehicle.objects.filter(owner_id=request.user.id)
	except:
		vehicles = None
	if request.method == 'POST':
		print(request.POST)
		form = VehicleForm(request.POST)
		if form.is_valid():
			next_url = request.POST.get('next')
			model_instance = form.save(commit=False)
			model_instance.timestamp = timezone.now()
			model_instance.save()
			return redirect('vehicle_index')
	else:
		form = VehicleForm()
	context = {
		'form': form,
		'vehicles': vehicles
	}
	return render(request, 'FuelTrackerApp/vehicle/new.html', context)

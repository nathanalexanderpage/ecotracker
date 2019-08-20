from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from .models import FuelStation, Receipt, Vehicle

# Create your views here.

app_url_ext = '/fuel'

# INDEX VIEWS
def index(request):
    context = {
        'subsite_base_url': app_url_ext
    }
    return render(request, 'FuelTrackerApp/index.html', context)

# AUTH VIEWS
def login(request):
    context = {
        'subsite_base_url': app_url_ext
    }
    return render(request, 'FuelTrackerApp/auth/login.html', context)
def signup(request):
    context = {
        'subsite_base_url': app_url_ext
    }
    return render(request, 'FuelTrackerApp/auth/signup.html', context)

# FUEL STATION VIEWS
def fuel_station_detail(request, fuel_station_id):
    try:
        fuel_station = FuelStation.objects.get(pk=fuel_station_id)
    except:
        raise Http404("Indicated fuel station does not exist")
    context = {
        'fuel_station': fuel_station
    }
    return render(request, 'FuelTrackerApp/fuel_station/detail.html', context)
def fuel_station_new(request):
    return HttpResponse("You're making a new gas station")

# RECEIPT VIEWS
def receipt_detail(request, receipt_id):
    try:
        print(0)
        print('Searching for Receipt object with pk=' + str(receipt_id))
        receipt = Receipt.objects.get(pk=receipt_id)
        print(receipt)
        print('Searching for FuelStation object with pk=' + str(receipt.gas_station_id))
        fuel_station = FuelStation.objects.get(pk=receipt.gas_station_id)
        print('Searching for Vehicle object with pk=' + str(receipt.vehicle_id))
        vehicle = Vehicle.objects.get(pk=receipt.vehicle_id)
        # print('Searching for User object with pk=' + str(vehicle.owner_id))
        # owner = settings.AUTH_USER_MODEL.objects.get(pk=receipt.owner_id)
    except:
        raise Http404("Indicated purchase does not exist")
    context = {
        'receipt': receipt,
        'fuel_station': fuel_station,
        'vehicle': vehicle,
        # 'owner': owner,
        'price_total': round((receipt.price_per_gal * receipt.gallons), 2)
    }
    return render(request, 'FuelTrackerApp/receipt/detail.html', context)
def receipt_new(request):
    return HttpResponse("You're inputting a new receipt")

# VEHICLE VIEWS
def vehicle_detail(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(pk=vehicle_id)
    except:
        raise Http404("Indicated fuel station does not exist")
    context = {
        'vehicle': vehicle
    }
    return render(request, 'FuelTrackerApp/vehicle/detail.html', context)
def vehicle_new(request):
    return HttpResponse("You're making a new vehicle")

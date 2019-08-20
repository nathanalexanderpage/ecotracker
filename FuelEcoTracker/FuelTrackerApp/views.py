from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from .models import FuelStation, Receipt, Vehicle

# Create your views here.

# INDEX VIEWS
def index(request):
    return render(request, 'FuelTrackerApp/index.html')

# AUTH VIEWS
def login(request):
    return render(request, 'FuelTrackerApp/auth/login.html')
def signup(request):
    return render(request, 'FuelTrackerApp/auth/signup.html')

# FUEL STATION VIEWS
def fuel_station_index(request):
    return render(request, 'FuelTrackerApp/fuel_station/index.html')
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
def receipt_index(request):
    return render(request, 'FuelTrackerApp/receipt/index.html')
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
def vehicle_index(request):
    return render(request, 'FuelTrackerApp/vehicle/index.html')
def vehicle_detail(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        receipts =  Receipt.objects.filter(vehicle_id=vehicle.id)
        print(receipts)
    except:
        raise Http404("Indicated vehicle does not exist")
    context = {
        'vehicle': vehicle,
        'receipts': receipts
    }
    return render(request, 'FuelTrackerApp/vehicle/detail.html', context)
def vehicle_new(request):
    try:
        vehicles = Vehicle.objects.all()
    except:
        vehicles = False
    context = {
        'vehicles': vehicles
    }
    return render(request, 'FuelTrackerApp/vehicle/new.html', context)

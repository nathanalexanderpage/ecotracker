from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import FuelStation, Receipt, Vehicle

# Create your views here.

def index(request):
    return HttpResponse("Hello world. This is Fuel Eco Tracker")

def fuel_station_detail(request, fuel_station_id):
    return HttpResponse("You're looking at gas station %s" % fuel_station_id)

def fuel_station_new(request):
    return HttpResponse("You're making a new gas station")

def receipt_detail(request, receipt_id):
    return HttpResponse("You're looking at receipt %s" % receipt_id)

def receipt_new(request):
    return HttpResponse("You're inputting a new receipt")

def vehicle_detail(request, vehicle_id):
    return HttpResponse("You're looking at vehicle %s" % vehicle_id)

def vehicle_new(request):
    return HttpResponse("You're making a new vehicle")

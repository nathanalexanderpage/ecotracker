from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date

# Create your models here.
class Vehicle(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    make = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    year = models.IntegerField()
    nickname = models.CharField(max_length=40)

class FuelStation(models.Model):
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)

class Receipt(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    gas_station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    receipt_date = models.DateField(default=date.today)
    receipt_time = models.TimeField(default=timezone.now)
    gallons = models.FloatField()
    price_per_gal = models.FloatField()
    is_cash_purchase = models.BooleanField()

from django.db import models
from django.conf import settings

# Create your models here.
class Receipt(models.Model):
    vehicle = models.ForeignKey(Vehicle)
    gas_station = models.ForeignKey('gas station', FuelStation)
    date = models.DateField(default=date.today)
    time = models.TimeField(default=timezone.now)
    gallons = models.FloatField()
    price_per_gal = models.FloatField('price per gallon')
    is_cash_purchase = models.BooleanField('cash purchase')

class Vehicle(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    make = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    year = models.IntegerField()
    nickname = models.CharField(max_length=40)

class FuelStation(models.Model):
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)

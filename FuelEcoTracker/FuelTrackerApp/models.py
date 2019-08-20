from datetime import date, datetime
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Vehicle(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    make = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    year = models.IntegerField()
    nickname = models.CharField(null=True, blank=True, max_length=40)

    def __str__(self):
        return ((self.nickname + ', ') if self.nickname else '') + ' ' + self.owner.username + '\'s ' + str(self.year) + ' ' + self.make + ' ' + self.model

class FuelStation(models.Model):
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=50)
    state_abbr = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.company + ' in ' + self.city + ', ' + self.state_abbr + ' @ ' + self.address + ' (' + self.zip_code + ')'

class Receipt(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    gas_station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    receipt_datetime = models.DateTimeField(default=datetime.now)
    # receipt_date = models.DateField(default=date.today)
    # receipt_time = models.TimeField(default=timezone.now)
    gallons = models.FloatField()
    price_per_gal = models.FloatField()
    mi_since_last = models.FloatField()
    is_cash_purchase = models.BooleanField()
    note = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        if self.vehicle.nickname:
            vehicle_name = self.vehicle.nickname + ' (' + self.vehicle.make + ' ' + self.vehicle.model + ')'
        else:
            vehicle_name = self.vehicle.make + ' ' + self.vehicle.model
        return self.vehicle.owner.username + '\'s ' + vehicle_name + ': ' + str(self.receipt_datetime)[:16] + ' @ ' + self.gas_station.company + ', ' + str(self.gallons) + 'gal w/ ' + ('cash' if self.is_cash_purchase else 'card') + ' — $' + str(round(self.gallons * self.price_per_gal, 2))

    def is_very_expensive(self):
        return price_per_gal > 3.9

    def is_very_cheap(self):
        return price_per_gal < 3.1

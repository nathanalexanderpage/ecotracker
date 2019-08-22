from datetime import date, datetime
from django.db import models
from django.conf import settings
# from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.
class Vehicle(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, help_text="The user to which this vehicle belongs")
    make = models.CharField(max_length=40, help_text="The manufacturer of the car. ex: Honda, Ford, Hyundai")
    model = models.CharField(max_length=40, help_text="The \"type\" of car. Name is given by the manufacturer. ex: (Honda) Civic, (Ford) F-150, (Hyundai) Elantra")
    year = models.IntegerField(default=1999, help_text="The year of manufacture.")
    nickname = models.CharField(null=True, blank=True, max_length=40, verbose_name="Name", help_text="The name commonly used to refer to this vehicle (if applicable)")

    def __str__(self):
        return ((self.nickname + ', ') if self.nickname else '') + ' ' + self.owner.username + '\'s ' + str(self.year) + ' ' + self.make + ' ' + self.model

    def is_recent_model(self):
        return self.year > datetime.today().year - 4

class FuelStation(models.Model):
    company = models.CharField(max_length=50, help_text="The company that owns the fuel station. ex: 7-Eleven, Shell, 79, Costco")
    address = models.CharField(max_length=80, help_text="Street address of the fuel station (number and street name portion)")
    city = models.CharField(max_length=50, help_text="City in which the fuel station is located")
    state_abbr = models.CharField(max_length=2, verbose_name="State (2-letter)", help_text="State's two-letter postal abbreviation. ex: NY, FL, ME, WA, CA")
    zip_code = models.CharField(max_length=5, help_text="Postal (zip) code portion of the fuel station's street address")
    latitude = models.FloatField(null=True, blank=True, help_text="Latitude coordinate of the fuel station")
    longitude = models.FloatField(null=True, blank=True, help_text="Longitude coordinate of the fuel station")

    def __str__(self):
        return self.company + ' in ' + self.city + ', ' + self.state_abbr + ' @ ' + self.address + ' (' + self.zip_code + ')'

class Receipt(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, help_text="Vehicle which received the fill-up")
    gas_station = models.ForeignKey(FuelStation, on_delete=models.CASCADE, verbose_name="Fuel station", help_text="Fuel station at which the fill-up was made")
    receipt_datetime = models.DateTimeField(default=datetime.now, verbose_name="Date & time", help_text="The date & time of the fill-up. Must format as: YYYY-MM-DD hh:mm:ss")
    # receipt_date = models.DateField(default=date.today)
    # receipt_time = models.TimeField(default=timezone.now)
    gallons = models.FloatField(help_text="The number of gallons purchased")
    price_per_gal = models.FloatField(help_text="The price per gallon of fuel")
    mi_since_last = models.FloatField(verbose_name="Miles driven since last", help_text="The number of miles driven since last fill-up")
    is_cash_purchase = models.BooleanField(verbose_name="Cash purchase", help_text="'Yes' indicates cash payment; 'No' indicates card payment.")
    note = models.CharField(null=True, blank=True, max_length=50, help_text="Optional small description accompanying the fill-up record")

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

from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import FuelStation, Receipt, Vehicle

class FuelStationForm(ModelForm):
    class Meta:
        model = FuelStation
        fields = ['id', 'company', 'address', 'city', 'state_abbr', 'zip_code']

class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = ['id', 'gallons', 'price_per_gal', 'is_cash_purchase', 'gas_station', 'vehicle', 'receipt_datetime', 'note', 'mi_since_last']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['id', 'make', 'model', 'year', 'nickname', 'owner']

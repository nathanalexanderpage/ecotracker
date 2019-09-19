from rest_framework import seializers
from .models import FuelStation, Receipt, Vehicle

# configure serializers here
class FuelStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelStation
        fields = ('id', 'company', 'address', 'latitude', 'longitude', 'city', 'state_abbr', 'zip_code')
class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ('id', 'gallons', 'price_per_gal', 'is_cash_purchase', 'gas_station_id', 'vehicle_id', 'receipt_datetime', 'note', 'mi_since_last')
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'make', 'model', 'year', 'nickname', 'owner_id')

from django.contrib import admin
from .models import Vehicle, Receipt, FuelStation


class VehicleAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['owner', 'nickname']}),
		('Specs', {'fields': ['make', 'model', 'year']})
	]

class ReceiptAdmin(admin.ModelAdmin):
	fieldsets = [
		('Basics', {'fields': ['vehicle', 'gas_station']}),
		('The Purchase', {'fields': ['receipt_datetime', 'gallons', 'price_per_gal', 'mi_since_last', 'is_cash_purchase']}),
		(None, {'fields': ['note']})
	]
class FuelStationAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['company']}),
		('Location', {'fields': ['address', 'city', 'state_abbr', 'zip_code', 'latitude', 'longitude']})
	]

# Register your models here.
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(FuelStation, FuelStationAdmin)

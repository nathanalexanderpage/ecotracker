from django.contrib import admin
from .models import Vehicle, Receipt, FuelStation

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Receipt)
admin.site.register(FuelStation)

from django.contrib import admin
from .models import Costumer
from .models import VehicleSize
from .models import VehicleType
from .models import Vehicle
from .models import Rental
from .models import RentalRate

# Register your models here.
admin.site.register(Costumer)
admin.site.register(VehicleSize)
admin.site.register(VehicleType)
admin.site.register(Vehicle)
admin.site.register(Rental)
admin.site.register(RentalRate)
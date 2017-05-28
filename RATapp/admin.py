from django.contrib import admin

# Register your models here.
from .models import User, Vehicle, Crash, CrashDescription, Service, Offer, HighOffer, LowOffer, Review

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'firstname', 'lastname', 'phone',)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('VIN', 'number', 'brand', 'model', 'year', 'user', 'is_auction')


admin.site.register(User, UserAdmin)
admin.site.register(Vehicle, VehicleAdmin)

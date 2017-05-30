from django.contrib import admin

# Register your models here.
from .models import User, Vehicle, Crash, CrashDescription, Service, Offer, HighOffer, LowOffer, Review

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'firstname', 'lastname', 'phone',)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'VIN', 'number', 'brand', 'model', 'year', 'user', 'is_auction')


class CrashAdmin(admin.ModelAdmin):
    list_display = ('id', 'actual', 'description_id', 'vehicle_id', 'date',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('VIN', 'number', 'brand', 'model', 'year', 'user', 'is_auction')




admin.site.register(User, UserAdmin)
admin.site.register(Vehicle, VehicleAdmin)

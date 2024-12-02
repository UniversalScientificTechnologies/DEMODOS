from django.contrib import admin
from .models import Group, Location, Detector, HistoricalData, Device

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

@admin.register(Detector)
class DetectorAdmin(admin.ModelAdmin):
    list_display = ("name", "group", "location", "cps", "threshold", "noise", "total_dose", "dose_rate", "alert", "set_dose_rate", "set_threshold", "set_noise")

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("unique_id", "name", "type", "last_connection", "ip_address", "battery_level", "charging_status", "fw_version", "detector")

@admin.register(HistoricalData)
class HistoricalDataAdmin(admin.ModelAdmin):
    list_display = ("detector_user", "timestamp", "dose")
from django.contrib import admin
from .models import Group, Location, Detector, HistoricalData

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

@admin.register(Detector)
class DetectorAdmin(admin.ModelAdmin):
    list_display = ("name", "group", "location", "current_cps", "set_cps", "set_threshold", "noise", "total_dose", "dose_rate", "alert")

@admin.register(HistoricalData)
class HistoricalDataAdmin(admin.ModelAdmin):
    list_display = ("detector_user", "timestamp", "dose")
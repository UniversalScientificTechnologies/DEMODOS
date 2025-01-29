from django.db import models
from django.utils.translation import gettext_lazy as _
import random


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    detailed_description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    detailed_description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Device(models.Model):
    class DeviceType(models.TextChoices):
        PAD = 'PAD', _('PAD')
        DDU = 'DDU', _('DDU')

    unique_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=3, choices=DeviceType.choices, default=DeviceType.PAD)

    last_connection = models.DateTimeField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    battery_level = models.IntegerField(default=None, null=True)
    battery_voltage = models.FloatField(default=None, null=True)
    wifi_rssi = models.FloatField(default=None, null=True)
    charging_status = models.BooleanField(default=None, null=True)
    fw_version = models.CharField(max_length=100, default=None, null=True)

    detector = models.ForeignKey("Detector", on_delete=models.SET_NULL, null=True, blank=True, related_name="devices")

    def __str__(self):
        return f"{self.type} - {self.unique_id}"

class Detector(models.Model):
    class DoseRateSource(models.TextChoices):
        LOCAL = "LOCAL", _("Local")
        GROUP = "GROUP", _("Group")
        LOCATION = "LOCATION", _("Location")

    
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name="detectors")
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name="detectors")

    data_source = models.CharField(max_length=10, choices=DoseRateSource.choices, default=DoseRateSource.LOCAL)

    set_dose_rate = models.FloatField(default=0.0)
    set_threshold = models.FloatField(default=0)
    set_noise = models.BooleanField(default=False)

    # Specifické hodnoty detektoru

    total_dose = models.FloatField(default=0.0)  # Celková dávka (mSv)
    dose_rate = models.FloatField(default=0.0)  # Dávková rychlost (μSv/h)
    cps = models.IntegerField(default=0)  # Impulsů za sekundu

    @property
    def threshold(self):
        return self.set_threshold

    @property
    def noise(self):
        return self.set_noise

    @property
    def alert(self):
        return self.dose_rate > self.threshold

    @property
    def ddu(self):
        return self.devices.filter(type="DDU")
    
    @property
    def pad(self):
        return self.devices.filter(type="PAD")

    def __str__(self):
        return self.name


class HistoricalData(models.Model):
    detector_user = models.ForeignKey(Detector, on_delete=models.CASCADE, related_name="historical_data")
    timestamp = models.DateTimeField(auto_now_add=True)
    dose = models.FloatField()

    def __str__(self):
        return f"Data for {self.detector_user.name} at {self.timestamp}"

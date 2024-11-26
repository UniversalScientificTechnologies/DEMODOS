from django.db import models


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


class Detector(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name="detectors")
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name="detectors")

    # Specifické hodnoty detektoru
    current_cps = models.IntegerField(default=0)  # Aktuální CPS
    set_cps = models.IntegerField(default=0)  # Nastavený CPS
    set_threshold = models.IntegerField(default=0)  # Prahová hodnota
    noise = models.BooleanField(default=False)  # Šum zapnuto/vypnuto
    total_dose = models.FloatField(default=0.0)  # Celková dávka (mSv)
    dose_rate = models.FloatField(default=0.0)  # Dávková rychlost (μSv/h)
    alert = models.BooleanField(default=False)  # Indikace alarmu

    def __str__(self):
        return self.name


class HistoricalData(models.Model):
    detector_user = models.ForeignKey(Detector, on_delete=models.CASCADE, related_name="historical_data")
    timestamp = models.DateTimeField(auto_now_add=True)
    dose = models.FloatField()

    def __str__(self):
        return f"Data for {self.detector_user.name} at {self.timestamp}"

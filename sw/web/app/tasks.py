# tasks.py
import os
import django
import time
from demodos_ui.models import Detector
import random


def background_task():
    while True:
        try:
            detectors = Detector.objects.all()
            print(f"Detectors: {detectors}", flush=True)
            for detector in detectors:
                print(f"Detector {detector.name}...", flush=True)
                detector.total_dose += detector.dose_rate / (60 * 60 / 10)
                
                if detector.noise:
                    detector.dose_rate = detector.set_dose_rate * random.gauss(1, 0.2)
                else:
                    detector.dose_rate = detector.set_dose_rate
                
                if detector.dose_rate <= 0:
                    detector.dose_rate = 0

                detector.cps = detector.dose_rate * 100 * random.gauss(1, 0.2)

                detector.save()
                
        except Exception as e:
            print(f"Chyba: {e}", flush=True)
        
        
        time.sleep(10)
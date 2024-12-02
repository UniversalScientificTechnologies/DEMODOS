from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from demodos_ui.models import Detector, HistoricalData
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from demodos_ui.models import Location, Group, Device, Detector

import datetime

from django.core.serializers import serialize
import json
import markdown
from django.shortcuts import render
from django.http import Http404
import os
from django.views import View


class DetectorConfig(View):
    def get(self, request, *args, **kwargs):
        detectors = Detector.objects.all().order_by('-active', 'id')

        return render(request, "detectors_config.html", {"detectors": detectors})
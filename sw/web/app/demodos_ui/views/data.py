from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from demodos_ui.models import Detector, HistoricalData
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from demodos_ui.models import Location, Group, Device

import datetime

from django.core.serializers import serialize
import json
import markdown
from django.shortcuts import render
from django.http import Http404
import os
from django.views import View


class DetectorData(View):
    def get(self, request, device, *args, **kwargs):
        if not device:
            return JsonResponse({'error': 'Detector ID is required'}, status=400)
        
        #device = get_object_or_create(Detector, unique_id=device)
        dev = Device.objects.get_or_create(unique_id=device)[0]


        status = {
            'id': dev.unique_id,
            'name': dev.unique_id,
            'type': dev.type,
            'group': None,
            'location': None,
        }

        status['name'] = dev.detector.name
        status['group'] = dev.detector.group.name if dev.detector.group else None
        status['location'] = dev.detector.location.name if dev.detector.location else None
        status['dose_rate'] = dev.detector.dose_rate
        status['total_dose'] = dev.detector.total_dose
        status['alert'] = int(dev.detector.alert)
        status['cps'] = dev.detector.cps


        dev.last_connection = datetime.datetime.now(datetime.timezone.utc)
        dev.ip_address = request.META.get('REMOTE_ADDR', None)
        dev.battery_level = request.GET.get('battery_level', None)
        dev.charging_status = request.GET.get('charging_status', None)

        dev.save()


        return JsonResponse(status)
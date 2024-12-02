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


class Settings(View):
    def get(self, request, *args, **kwargs):
        if not device:
            return JsonResponse({'error': 'Detector ID is required'}, status=400)
        
        #device = get_object_or_create(Detector, unique_id=device)
        dev = Device.objects.get_or_create(unique_id=device)[0]
        status = {
            'id': dev.unique_id,
            'name': dev.name,
            'created': dev.created_at,
            'type': dev.type,
            'last_connection': dev.last_connection,
            'battery_level': dev.battery_level,
            'ip_address': dev.ip_address,
            'charging_status': dev.charging_status
        }

        dev.last_connection = datetime.datetime.now(datetime.timezone.utc)
        dev.ip_address = request.META.get('REMOTE_ADDR', None)
        dev.battery_level = request.GET.get('battery_level', None)
        dev.charging_status = request.GET.get('charging_status', None)

        dev.save()


        return JsonResponse(status)
    
class DeviceList(View):
    def get(self, request, *args, **kwargs):
        devices = Device.objects.all()

        return render(request, "devices_list.html", {"devices": devices})
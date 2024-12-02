from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from demodos_ui.models import Detector, HistoricalData
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from demodos_ui.models import Location, Group, Device, Detector
from demodos_ui.forms import DeviceForm, DetectorForm


from django.core.serializers import serialize
import json
import markdown
from django.shortcuts import render, redirect
from django.http import Http404
import os
from django.views import View

def home(request):
    return render(request, "home.html")

def detector_dashboard(request):
    users = Detector.objects.filter(active=True).order_by("id")
    return render(request, "dashboard.html", {"users": users})

def update_dose(request, user_id):
    if request.method == "POST":
        dose = float(request.POST.get("dose"))
        user = get_object_or_404(Detector, id=user_id)
        user.current_dose = dose
        user.save()
        return JsonResponse({"status": "success", "dose": user.current_dose})

def clear_historical_data(request):
    if request.method == "POST":
        HistoricalData.objects.all().delete()
        return JsonResponse({"status": "success"})

@csrf_exempt
def update_params(request, entity_type, entity_id):

    print("entity_type", entity_type, flush=True)
    print("entity_id", entity_id, flush=True)


    if request.method == "POST":
        # Rozlišit typ entity
        if entity_type == "detector":
            entity = get_object_or_404(Detector, id=entity_id)
        elif entity_type == "location":
            entity = get_object_or_404(Location, id=entity_id)
        elif entity_type == "group":
            entity = get_object_or_404(Group, id=entity_id)
        else:
            return HttpResponse("Invalid entity type", status=400)

        # Show all arguments
        print("request.POST:", request.POST, flush=True)

        # Aktualizace CPS (pro detektor), threshold (pro lokalitu nebo skupinu)
        if "set_dose_rate" in request.POST:
            entity.set_dose_rate = float(request.POST.get("set_dose_rate", entity.set_dose_rate))
            print("entity.set_dose_rate", entity.set_dose_rate, flush=True)
        if "set_threshold" in request.POST:
            entity.set_threshold = float(request.POST.get("set_threshold", entity.set_threshold))
            print("entity.set_threshold", entity.set_threshold, flush=True)
        if "set_noise" in request.POST:
            sn = request.POST.get("set_noise", entity.set_noise)
            if sn is "on":
                entity.set_noise = True
            elif sn is "off":
                entity.set_noise = False
            print("entity.set_noise", entity.set_noise, flush=True)
        
        entity.save()

        return HttpResponse("Ok")


def data_endpoint(request):
    id = request.GET.get("detector_id")
    user = Detector.objects.filter(id=id).first()
    return render(request, "partials/detector_box.html", {"user": user})


def get_data(request):
    dets = Detector.objects.filter(active=True).order_by("id")
    
    dets = [
        {
            "id": d.id,
            "name": d.name,
            "dose_rate": d.dose_rate,
            "total_dose": d.total_dose,
            "cps": d.cps,
            "set_threshold": d.set_threshold,
            "set_dose_rate": d.set_dose_rate,
            "noise": d.noise,
            "alert": d.alert,
        }
        for d in dets
    ]
    
    data = {"detectors": dets}
    
    return JsonResponse(data)
    
    

def settings(request):
    return render(request, "settings.html")


DOCUMENTATION_DIR = os.path.join(os.path.dirname(__file__), 'docs')
def docs(request, filename="index"):
    filepath = os.path.join(DOCUMENTATION_DIR, f"{filename}.md")

    if not os.path.exists(filepath):
        filepath = os.path.join(DOCUMENTATION_DIR, "404.md")

    with open(filepath, "r", encoding="utf-8") as file:
        markdown_content = file.read()

    # Převod Markdown na HTML
    html_content = markdown.markdown(markdown_content)

    return render(request, "documentation.html", {"content": html_content})


class detector_info(View):
    def get(self, request, detector_id):
        detector = get_object_or_404(Detector, id=detector_id)
        
        return render(request, "partials/detector_box_info.html", {"user": detector})
    


class detector_edit(View):
    def get(self, request, detector_id):
        
        if detector_id == 0:
            detector = Detector()
        else:
            detector = Detector.objects.get(id=detector_id)
        
        form = DetectorForm(instance=detector)
        
        return render(request, "detector_edit.html", {"user": detector, "form": form, "detector_id": detector.id})
    
    def post(self, request, detector_id):
        if detector_id == 0:
            detector = Detector()
        else:
            detector = Detector.objects.get(id=detector_id)
        
        # detector.name = request.POST.get("name", detector.name)
        # detector.dose_rate = request.POST.get("dose_rate", detector.dose_rate)
        # detector.total_dose = request.POST.get("total_dose", detector.total_dose)
        # detector.cps = request.POST.get("cps", detector.cps)
        # detector.set_threshold = request.POST.get("set_threshold", detector.set_threshold)
        # detector.set_dose_rate = request.POST.get("set_dose_rate", detector.set_dose_rate)
        # detector.save()

        form = DetectorForm(request.POST, instance=detector)
        
        if form.is_valid():
            form.save()
            return render(request, "detector_edit.html", {"user": detector, "form": form, "detector_id": detector.id, "status": "ok", "message": "Data saved"})
        else:
            return render(request, "detector_edit.html", {"user": detector, "form": form, "detector_id": detector.id, "status": "err", "message": "Data not saved"})

class detector_delete(View):
    def get(self, request, detector_id):
        detector = get_object_or_404(Detector, id=detector_id)
        detector.delete()

        return redirect("detector_list")
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from demodos_ui.models import Detector, HistoricalData
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from demodos_ui.models import Location, Group

from django.core.serializers import serialize
import json
import markdown
from django.shortcuts import render
from django.http import Http404
import os

def home(request):
    return render(request, "home.html")

def detector_dashboard(request):
    users = Detector.objects.all().order_by("id")
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
        if hasattr(entity, "set_cps"):
            entity.set_cps = int(request.POST.get("set_cps", entity.set_cps))
            print("entity.set_cps", entity.set_cps, flush=True)
        if hasattr(entity, "set_threshold"):
            entity.set_threshold = int(request.POST.get("set_threshold", entity.set_threshold))
            print("entity.set_threshold", entity.set_threshold, flush=True)
        if hasattr(entity, "set_noise"):
            sn = request.POST.get("set_noise", entity.set_noise)
            if sn is "on":
                entity.set_noise = True
            elif sn is "off":
                entity.set_noise = False
            print("entity.set_noise", entity.set_noise, flush=True)
        
        entity.save()

        # Vracíme odpověď (hodnota nebo potvrzení)
        return HttpResponse(entity.set_cps if hasattr(entity, "set_cps") else entity.set_threshold)


def data_endpoint(request):
    id = request.GET.get("detector_id")
    print("ID", id)
    user = Detector.objects.filter(id=id).first()
    print("USER", user)
    return render(request, "partials/detector_box.html", {"user": user})


def get_data(request):
    dets = Detector.objects.all().order_by("id")
    
    dets = serialize('json', dets)
    dets = [d["fields"] for d in json.loads(dets)]
    
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
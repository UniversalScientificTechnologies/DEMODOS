from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from demodos_ui.models import Detector, HistoricalData
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from demodos_ui.models import Location, Group

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
def update_cps(request, entity_type, entity_id):
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

        # Aktualizace CPS (pro detektor), threshold (pro lokalitu nebo skupinu)
        if hasattr(entity, "current_cps"):
            entity.current_cps = int(request.POST.get("cps", entity.current_cps))
        elif hasattr(entity, "threshold"):
            entity.threshold = int(request.POST.get("threshold", entity.threshold))
        entity.save()

        # Vracíme odpověď (hodnota nebo potvrzení)
        return HttpResponse(entity.current_cps if hasattr(entity, "current_cps") else entity.threshold)


def data_endpoint(request):
    id = request.GET.get("id")
    users = Detector.objects.filter(id=id).first()
    return render(request, "partials/detector_box.html", {"users": users})
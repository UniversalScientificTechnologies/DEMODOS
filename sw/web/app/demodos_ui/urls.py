"""
URL configuration for demodos_ui project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import dashboard, data, devices, detectors

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", dashboard.home, name="detector_dashboard"),
    path("dashboard/", dashboard.detector_dashboard, name="detector_dashboard"),
    path("detector/<int:detector_id>/get-info/", dashboard.detector_info.as_view(), name="detector_info"),
    path("detector/<int:detector_id>/edit/", dashboard.detector_edit.as_view(), name="detector_edit"),
    path("detector/<int:detector_id>/delete/", dashboard.detector_delete.as_view(), name="detector_delete"),
    path("settings/devices/", devices.DeviceList.as_view(), name="settings_devices"),
    path("settings/detectors/", detectors.DetectorConfig.as_view(), name="detector_list"),
    path("data/<str:device>/", data.DetectorData.as_view(), name="data"),
    path("docs/", dashboard.docs, name="docs"),
    path("docs/<str:filename>/", dashboard.docs, name="docs"),
    path("update-dose/<int:user_id>/", dashboard.update_dose, name="update_dose"),
    path("data-endpoint/", dashboard.data_endpoint, name="data_endpoint"),
    path("clear-data/", dashboard.clear_historical_data, name="clear_data"),
    path("get_data/", dashboard.get_data, name="get_data"),
    path("<str:entity_type>/<int:entity_id>/update-cps/", dashboard.update_params, name="update_cps"),
    path("<str:entity_type>/<int:entity_id>/update-threshold/", dashboard.update_params, name="update_threshold"),
    path("<str:entity_type>/<int:entity_id>/update-noise/", dashboard.update_params, name="update_noise"),


]

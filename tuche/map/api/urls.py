from django.urls import path

from map.api.views import api_create_report

app_name = 'map'

urlpatterns = [
    path('create', api_create_report, name="create"),


]
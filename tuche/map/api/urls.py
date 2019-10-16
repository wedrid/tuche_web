from django.urls import path

from map.api.views import api_create_report
from map.api.views import api_get_data

app_name = 'map'

urlpatterns = [
    path('create', api_create_report, name="create"),
    path('get_data', api_get_data , name='get_data')
]
from django.shortcuts import render
from django.http import HttpResponse
from .models import Report

# Create your views here.

alerts = [
    {
        'autore': 1,
        'lat': 42,
        'lon': 11,
        'data': 'Lunedì'
    },
    {
        'autore': 2,
        'lat': 42.1,
        'lon': 11.2,
        'data': 'Martedì'
    },
    {
        'autore': 3,
        'lat': 42.3,
        'lon': 11.3,
        'data': 'Mercoledì'
    }
]

def home(request):
    # context viene passata 
    context = {
        'rows' : Report.objects.all()
    }

    return render(request, 'map/home.html', context)
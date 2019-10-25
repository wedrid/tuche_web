from django.shortcuts import render
from django.http import HttpResponse
from .models import Report
from django.db.models.expressions import F
from django.db.models.functions.math import Sqrt, Power
from django.core.paginator import Paginator

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
    rows = Report.objects.all()

    paginator = Paginator(Report.objects.all(), 8)

    page = request.GET.get('page')

    righe = paginator.get_page(page)


    context = {
        'rows' : Report.objects.all(),
        'righe': righe
    }

    return render(request, 'map/home.html', context)

def maponly(request):

    rows = Report.objects.all()
    
    context = {
        'rows' : Report.objects.all()
    }

    return render(request, 'map/maponly.html', context);
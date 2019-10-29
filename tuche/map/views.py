from django.shortcuts import render
from django.http import HttpResponse
from .models import Report
from django.db.models.expressions import F
from django.db.models.functions.math import Sqrt, Power
from django.core.paginator import Paginator
from django.core import serializers

# Create your views here.

def registro(request):
    # context viene passata 
    # rows = Report.objects.all()

    paginator = Paginator(Report.objects.all(), 8)

    page = request.GET.get('page')

    righe = paginator.get_page(page)


    context = {
        'rows' : Report.objects.all(),
        'righe': righe
    }

    return render(request, 'map/logs.html', context)


def home(request):
    # context viene passata 
    # rows = Report.objects.all()

    paginator = Paginator(Report.objects.all(), 8)

    page = request.GET.get('page')

    righe = paginator.get_page(page)
    
    tmp = list(Report.objects.all())

    rowsjs = serializers.serialize("json", Report.objects.all())

    context = {
        'rows' : Report.objects.all(),
        'righe': righe,
        'rows_js': rowsjs,
    }

    return render(request, 'map/home.html', context)

def maponly(request):

    rows = Report.objects.all()
    
    context = {
        'rows' : Report.objects.all()
    }

    return render(request, 'map/maponly.html', context);
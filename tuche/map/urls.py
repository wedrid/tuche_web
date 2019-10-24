from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tuche-home'), #se è vuoto è perchè è la homepage
    path('maponly', views.maponly, name  ='tuche-maponly'),
]
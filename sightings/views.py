from django.shortcuts import render
from django.http import HttpResponse

from .models import Squirrel

def map(request):
    context={
        sightings:[{latitude:-73.9561344937861 , longitude:40.7940823884086}]
            }
    return render(request, 'map/map.html', context)

def sightings(request):
    return HttpResponse('Sightings')

def index(request):
    return HttpResponse('Home Index Page')

def detail(request):
    return HttpResponse('detail')

def add(request):
    return HttpResponse('add')

def stat(request):
    return HttpResponse('stat')
# Create your views here.

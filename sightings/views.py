from django.shortcuts import render
from django.http import HttpResponse

from .models import Squirrel

def map(request):
    squirrels = Squirrel.objects.all()[:75]
    context = {'squirrels': squirrels}
    return render(request, 'sightings/map.html', context)


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

from django.shortcuts import render
from django.http import HttpResponse

from .models import Squirrel

def map(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {'squirrels': squirrels}
    return render(request, 'sightings/map.html', context)


def sightings(request):
    squirrels = Squirrel.objects.all()
    context = {'squirrels': squirrels}
    return render(request, 'sightings/sightings.html', context)

def index(request):
    squirrels = Squirrel.objects.all()
    context = {'squirrels': squirrels}
    return render(request, 'sightings/base.html', context)

def detail(request):
    return HttpResponse('detail')

def add(request):
    return HttpResponse('add')

def stat(request):
    return HttpResponse('stat')
# Create your views here.

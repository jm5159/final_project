from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Squirrel
from .forms import UpdateRequestForm

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

def detail(request, unique_squirrel_id):
    squirrel = get_object_or_404(Squirrel, pk=unique_squirrel_id)
    context = {
        'squirrel': squirrel,
    }
    return render(request, 'sightings/detail.html', context)

def add(request):
    return HttpResponse('add')

def stat(request):
    return HttpResponse('stat')

def request_update(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({})

def request_add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({})
# Create your views here.


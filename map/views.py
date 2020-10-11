from django.shortcuts import render
from django.http import HttpResponse

from .models import Squirrel

def index(request):
    return HttpResponse('Hello')

# Create your views here.

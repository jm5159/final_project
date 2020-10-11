from django.shortcuts import render
from django.http import HttpResponse

from .models import Squirrel

def index(request):
    return HttpResponse('Hello')

def detail(request):
    return HttpResponse('Hello')

def add(request):
    return HttpResponse('Hello')

def stat(request):
    return HttpResponse('Hello')
# Create your views here.

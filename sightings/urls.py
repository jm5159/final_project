from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('sightings/', views.sightings, name='sightings'),
    path('sightings/detail/', views.detail, name='detail'),
    path('sightings/add/', views.add, name='add'),
    path('sightings/stat/', views.stat, name='stat'),
    path('map/', views.map, name = 'map'),
]

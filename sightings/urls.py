from django.urls import path

from . import views

from django.urls import path

from . import views

app_name = 'sightings-view'

urlpatterns = [
    path('', views.index, name='index'),    
    path('sightings/', views.sightings, name='sightings'),
    path('sightings/<str:unique_squirrel_id>/', views.detail, name='detail'),
    path('sightings/add/', views.add, name='add'),
    path('sightings/stat/', views.stat, name='stat'),
    path('map/', views.map, name = 'map'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.location, name='locations'),
    path('get-nearby-location/', views.get_nearby_location, name='get_nearby_location'),
    path('get-sorted-location/', views.get_cities_sorted_location, name='get_sorted_location'),
]
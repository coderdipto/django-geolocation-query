import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

from location.models import Location

latlang = lambda req: (float(req.GET.get('latitude')), float(req.GET.get('longitude')))
serializer = lambda l: {"name": l.name, "longitude": l.point.y, "latitude": l.point.x}
serializer_distance = lambda l: {"name": l.name, "longitude": l.point.y, "latitude": l.point.x, "distance": "{:.2f}".format(float(l.distance.m/1000)) }

def location(request):
    """
    Home page
    """
    template = 'location.html'
    locations = Location.objects.all()[:1500]
    location_dict = json.dumps([serializer(location) for location in locations])
    return render(request, template, locals())

def get_nearby_location(request):
    """
    Getting nearby cities within 100 KM radius
    """
    latitude, longitude = latlang(request)
    point = Point(float(longitude), float(latitude), srid=4326)
    locations = Location.objects.filter(point__distance_lte=(point, D(km=100)))
    return JsonResponse(json.dumps([serializer(location) for location in locations]), safe=False)

def get_cities_sorted_location(request):
    """
    Getting nearest cities sorted by distance from current location within 200 KM radius
    """
    latitude, longitude = latlang(request)
    point = Point(float(longitude), float(latitude), srid=4326)
    locations = Location.objects.filter(point__distance_lte=(point, D(km=200))).annotate(distance=Distance("point", point)).order_by("distance")[:10]
    return JsonResponse(json.dumps([serializer_distance(location) for location in locations]), safe=False)

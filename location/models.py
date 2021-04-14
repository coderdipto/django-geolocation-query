from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Location(models.Model):
    name = models.CharField(max_length=255, unique=True)
    point = models.PointField(srid=4326, blank=True, null=True)

    def __str__(self):
        # Latitude, Longitude
        return f"{self.point.x},{self.point.y}"

import os
import csv
from django.conf import settings
from django.db import transaction
from django.db import IntegrityError
from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand

from location.models import Location


class Command(BaseCommand):
    help = "Seed database for testing and development."

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        self.run_seed()
        self.stdout.write('done.')

    def run_seed(self):
        file = os.path.join(settings.BASE_DIR, 'worldcities.csv')
        
        with open(file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            for row in csv_reader:
                with transaction.atomic():
                    try:
                        Location.objects.create(
                            name=row['city'], 
                            point=Point(float(row['lng']), float(row['lat']), srid=4326)
                        )
                    except IntegrityError as e:
                        pass

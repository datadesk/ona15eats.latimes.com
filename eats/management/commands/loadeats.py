import os
import csv
from django.conf import settings
from geopy.distance import vincenty
from eats.models import Restaurant, Nerd
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load our restaurants, etc into the database'
    
    def handle(self, *args, **options):
        # First, wipe what we have
        Restaurant.objects.all().delete()
        # read our data CSV into memory
        csv_path = os.path.join(settings.BASE_DIR, 'eats', 'data', 'food.csv')
        data = list(csv.DictReader(open(csv_path)))
        # Loop through each item and load it into the database
        for i in data:
            # See which category this place falls in
            if i.get('Restaurant'):
                name = i.get('Restaurant')
                category = 'eats'

            elif i.get('Bar'):
                name = i.get('Bar')
                category = 'bars'

            elif i.get('Extracurricular'):
                name = i.get('Extracurricular')
                category = 'extras'

            # Grab our Nerd
            if i['Nerd'] == 'Gold':
                person = 'Jonathan Gold'
            else:
                person = i['Nerd']

            nerd = Nerd.objects.get(name__icontains=person)
            # Measure the distance
            distance = None
            hotel = (34.057449, -118.415886)
            lat = i['Latitude']
            lng = i['Longitude']
            if lat and lng:
                place = (float(lat), float(lng))
                distance = vincenty(hotel, place).miles

            Restaurant.objects.create(
                name=name,
                lat=lat,
                lng=lng,
                address=i['address'],
                description=i['Why you like it'],
                distance=distance,
                restaurant_url=i['URL'],
                photo_url=i['Image'],
                photo_credit=i['Image credit'],
                nerd=nerd,
                category=category,
            )

        print "Done"
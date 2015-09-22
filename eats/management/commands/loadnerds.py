import os
import csv
from eats.models import Nerd
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load all of our nerds into the database'
    
    def handle(self, *args, **options):
        # First, wipe what we have
        Nerd.objects.all().delete()
        # read our data CSV into memory
        csv_path = os.path.join(settings.BASE_DIR, 'eats', 'data', 'nerds.csv')
        data = list(csv.DictReader(open(csv_path)))
        # Loop through each item and load it into the database
        for i in data:
            Nerd.objects.create(
                name=i['name'],
                title=i['title'],
                image_url=i['image'],
                nerd_bio_url=i['url'],
            )

        print "Done"
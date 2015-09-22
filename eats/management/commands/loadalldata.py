import os
import csv
from eats.models import Nerd
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'meta command to load the nerds then eats'
    
    def handle(self, *args, **options):
        call_command('loadnerds')
        call_command('loadeats')
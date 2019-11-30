from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import requests, csv, re, sys
from dateutil import parser
from datetime import date

class Command(BaseCommand):
    help ='Import squirrel data from NYC Central Park'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='path of file to be imported')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        
        pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')

        with open(path, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                i,j,k = pattern.match(row.get('Date')).groups()
                obj, created = Squirrel.objects.get_or_create(
                    X = row.get('X'),
                    Y = row.get('Y'),
                    Unique_Squirrel_ID = row.get('Unique Squirrel ID'),
                    Hectare = row.get('Hectare'),
                    Shift = row.get('Shift'),
                    Date = date(int(k),int(i),int(j)),
                    Hectare_Squirrel_Number = row.get('Hectare Squirrel Number'),
                    Age = row.get('Age'),
                    Primary_Fur_Color = row.get('Primary Fur Color'),
                    Highlight_Fur_Color = row.get('Highlight Fur Color'),
                    Combination_Fur = row.get('Combination of Primary and Highlight Color'),
                    Color_Notes = row.get('Color Notes'),
                    Location = row.get('Location'),
                    Specific_Location = row.get('Specific Location'),
                    Running = row.get('Running'),
                    Chasing = row.get('Chasing'),
                    Climbing = row.get('Climbing'),
                    Eating = row.get('Eating'),
                    Foraging = row.get('Foraging'),
                    Other_Activities = row.get('Other Activities'),
                    Kuks = row.get('Kuks'),
                    Quaas = row.get('Quaas'),
                    Moans = row.get('Moans'),
                    Tail_Flags = row.get('Tail flags'),
                    Tail_Twitches = row.get('Tail twitches'),
                    Approaches = row.get('Approaches'),
                    Indifferent = row.get('Indifferent'),
                    Runs_From = row.get('Runs from'),
                    Other_Interactions = row.get('Other Interactions'),
                )
        print('Done!')

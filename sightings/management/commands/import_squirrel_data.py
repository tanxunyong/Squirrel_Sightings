from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import requests, csv, re
from dateutil import parser
from datetime import date

class Command(BaseCommand):
    help ='Import squirrel data from NYC Central Park'

    def handle(self, *args, **kwargs):
        dls = "https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv?accessType=DOWNLOAD&bom=true&format=true"
        resp = requests.get(dls)
        with open('squirrel_data.xls', 'wb') as output:
            output.write(resp.content)
            output.close
        
        pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')

        with open('squirrel_data.xls', newline='') as csvfile:
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
                    )
                print(row['Unique Squirrel ID'])
        print('Done!')

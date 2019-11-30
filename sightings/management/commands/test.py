from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import csv

class Command(BaseCommand):
    help = 'exports all fields'

    def handle(self, *args, **kwargs):
        with open('export_squirrel_data.csv', mode='w') as csvfile:
            writer = csv.writer(csvfile, delimiter = ',')
            all_fields = [f.name for f in Squirrel._meta.get_fields()]
            writer.writerow(all_fields[1:])
            for j in range(len(Squirrel.objects.all())-1):
                rowval=list()
                for i in all_fields:
                    if i == 'id': continue
                    rowval.append(getattr(Squirrel.objects.all()[0],i))
                writer.writerow(rowval)
        csvfile.close

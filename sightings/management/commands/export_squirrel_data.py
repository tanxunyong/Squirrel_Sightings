from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import csv

class Command(BaseCommand):
    help = 'exports all fields'
    
    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='path of file to be exported')
    
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        
        with open(path, mode='w',newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter = ',')
            all_fields = [f.name for f in Squirrel._meta.get_fields()]
            fieldnames = [Squirrel._meta.get_field(i).help_text for i in all_fields]
            writer.writerow(fieldnames)
            for j in range(len(Squirrel.objects.all())):
                rowval=list()
                for i in all_fields:
                    if i == 'id': continue
                    if i == 'Date':
                          rowval.append(str(getattr(Squirrel.objects.all()[j],i).strftime("%m%d%Y")))
                    else:
                        rowval.append(getattr(Squirrel.objects.all()[j],i))
                writer.writerow(rowval)
        csvfile.close

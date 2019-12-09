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
        
        all_fields = [f.name for f in Squirrel._meta.get_fields()]
        fieldnames = [Squirrel._meta.get_field(i).help_text for i in all_fields]
        
        pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')
        
        with open(path, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            USID = set() #keep record of USID that have already been imported
            all_fields = [f.name for f in Squirrel._meta.get_fields()] #get all the csv names
            fieldnames = [Squirrel._meta.get_field(i).help_text for i in all_fields] #get the model attribute names
            for row in reader:
                context = dict()
                if row.get('Unique Squirrel ID') in USID: 
                    continue #ignore the row if USID is a repeat of an existing. Unique ID cannot be repeated
                else:
                    i,j,k = pattern.match(row.get('Date')).groups()
                    for l in range(len(all_fields)):
                        if fieldnames[l] == 'Date':
                            context[all_fields[l]]=date(int(k),int(i),int(j))
                        else:
                            context[all_fields[l]]=row.get(fieldnames[l])
                    obj, created = Squirrel.objects.get_or_create(**context)
                USID.add(row.get('Unique Squirrel ID'))
        print('Done!')

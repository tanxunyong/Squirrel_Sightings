from django.shortcuts import render

from sightings.models import Squirrel

def map(request,*args,**kwargs):
    sightings = Squirrel.objects.all()[:20]
    context={
        'sightings':sightings        
    }     
    return render(request,'map/map.html',context)

# Create your views here.

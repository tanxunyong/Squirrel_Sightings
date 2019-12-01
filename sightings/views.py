from django.shortcuts import render
from django.http import HttpResponse

from .models import Squirrel

def sightings_view(request,*args,**kwargs):
    squirrels = Squirrel.objects.all()
    context={
        'squirrels':squirrels        
    }
    return render(request,'sightings/sightings_list.html',context)
# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .forms import SightingsForm

from .models import Squirrel


def sightings_edit_view(request):
    form = SightingsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form':form        
    }
    return render(request,'sightings/edit.html',context)

def sightings_view(request,*args,**kwargs):
    squirrels = Squirrel.objects.all()
    context={
        'squirrels':squirrels        
    }
    return render(request,'sightings/sightings_list.html',context)

def edit_view(request, sq_id):
    form = SightingsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context ={
        'form':form      
    }
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=sq_id)
    return render(request, 'sightings/edit.html', context)
    # Create your views here.

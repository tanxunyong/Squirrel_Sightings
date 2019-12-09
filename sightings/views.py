from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.db.models import Avg, Max, Min, Count

from .forms import SightingsForm

from .models import Squirrel

class add_view(CreateView):
    model = Squirrel
    fields = '__all__'
    success_url = reverse_lazy('sightings:sightings')

class delete_view(DeleteView):
    model = Squirrel
    success_url = reverse_lazy('sightings:sightings')

def main(request):
    return render(request,'sightings/main.html', {})

def sightings_view(request,*args,**kwargs):
    squirrels = Squirrel.objects.all()
    fields = ['Unique_Squirrel_ID','Date','Lat_Long']
    context={
        'squirrels':squirrels,
        'fields':fields,
    }    
    return render(request,'sightings/sightings_list.html',context)

def edit_view(request, sq_id):

    sqrl = Squirrel.objects.get(Unique_Squirrel_ID=sq_id)
    if request.method == 'POST':
        form = SightingsForm(request.POST, instance=sqrl)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SightingsForm(instance=sqrl)
    
    context ={
        'form':form,
        'sqid':sq_id,
    }
    return render(request, 'sightings/edit.html', context)

def stats(request):
    squirrels = Squirrel.objects.all()
    counts=len(squirrels)
    a=squirrels.aggregate(min_latitude=Min('Y'),max_latitude=Max('Y'),average_latitude=Avg('Y'))
    b=squirrels.aggregate(min_longitude=Min('X'),max_longitude=Max('X'),average_longitude=Avg('X'))
    c=list(squirrels.values_list('Shift').annotate(Count('Shift')))
    d=list(squirrels.values_list('Age').annotate(Count('Age')))
    e=list(squirrels.values_list('Primary_Fur_Color').annotate(Count('Primary_Fur_Color')))
    return render(request, 'sightings/sightings_stats.html', {"squirrels":squirrels,"counts":counts,"a":a,"b":b,"c":c,"d":d,"e":e })



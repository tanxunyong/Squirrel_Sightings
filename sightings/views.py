from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


from .forms import SightingsForm

from .models import Squirrel

class add_view(CreateView):
    model = Squirrel
    fields = '__all__'
    success_url = reverse_lazy('sightings:sightings')

class delete_view(DeleteView):
    model = Squirrel
    success_url = reverse_lazy('sightings:sightings')

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
    context={
        'squirrels':squirrels        
    }
 
    return render(request,'sightings/sightings_stats.html',context)

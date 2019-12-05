from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 1cd0a04... Add map and delete view.
=======

>>>>>>> feature5

from .forms import SightingsForm

from .models import Squirrel

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 1cd0a04... Add map and delete view.
class add_view(CreateView):
    model = Squirrel
    fields = '__all__'

class delete_view(DeleteView):
    model = Squirrel
    success_url = reverse_lazy('sightings:sightings')
 #   def get_success_url(self):
  #    return reverse('sightings', kwargs={'Unique_Squirrel_ID': self.object.Unique_Squirrel_ID})

<<<<<<< HEAD
=======
>>>>>>> a84e14a... Edit sightings/views to load existing object
=======
>>>>>>> 1cd0a04... Add map and delete view.
def sightings_view(request,*args,**kwargs):
    squirrels = Squirrel.objects.all()
    context={
        'squirrels':squirrels        
    }
    return render(request,'sightings/sightings_list.html',context)

def edit_view(request, sq_id):

    instance = get_object_or_404(Squirrel, Unique_Squirrel_ID=sq_id)
    form = SightingsForm(request.POST or None,instance=instance)
    if form.is_valid():
        form.save()
    
    context ={
        'form':form,
        'sqid':sq_id,
    }
    return render(request, 'sightings/edit.html', context)
<<<<<<< HEAD

def stats(request):
    squirrels = Squirrel.objects.all()
    context={
        'squirrels':squirrels        
    }
 
    return render(request,'sightings/sightings_stats.html',context)



<<<<<<< HEAD

=======
    # Create your views here.

#def add_view(request):
 #   return render(request, 'sightings/add.html',{})
>>>>>>> 1cd0a04... Add map and delete view.
=======

>>>>>>> feature5

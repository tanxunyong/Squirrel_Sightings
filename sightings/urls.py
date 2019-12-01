from django.urls import path

from . import views


app_name = 'sightings'
urlpatterns = [
        path('sightings/',sightings_view,name='sightings'),
        ]

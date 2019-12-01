from django.urls import path

from . import views


app_name = 'sightings'
urlpatterns = [
        path('',views.sightings_view,name='sightings'),
        path('<str:sq_id>',views.edit_view,name='edit'),
        ]

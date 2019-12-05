from django.urls import path

from . import views


app_name = 'sightings'
urlpatterns = [
        path('',views.sightings_view,name='sightings'),
        path('<str:sq_id>',views.edit_view,name='edit'),
        path('add/', views.add_view.as_view(), name='add'),
        path('<str:pk>/delete/', views.delete_view.as_view(),name='delete'),
        path('stats/',views.stats,name='stats'),
        ]

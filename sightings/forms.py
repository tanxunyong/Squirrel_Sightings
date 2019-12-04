from django import forms

from .models import Squirrel

class SightingsForm(forms.ModelForm): 
    class Meta:
        model = Squirrel
        all_fields = [f.name for f in Squirrel._meta.get_fields()]
        formfields = ', '.join(["'{}'".format(str(i)) for i in all_fields])
        print(formfields)
        fields = [
                'X','Y','Unique_Squirrel_ID','Hectare','Shift','Date',
                ]

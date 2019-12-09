from django import forms

from .models import Squirrel

class SightingsForm(forms.ModelForm): 
    class Meta:
        model = Squirrel
        all_fields = [f.name for f in Squirrel._meta.get_fields()]
        fields = []
        fields.extend(all_fields)

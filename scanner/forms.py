from django import forms
from .models import Rack

class RackSelectForm(forms.ModelForm):
    class Meta:
        model=Rack
        fields=['name']
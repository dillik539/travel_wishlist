from django import forms
from .models import Place

'''this file describes form'''

class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')

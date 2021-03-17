from django import forms

from .models import Motorista

class RawMotoristaForm(forms.Form):
    nombre = forms.CharField(required=True, label ='')
    apellido = forms.CharField(required=False, label='')
    email = forms.EmailField(required=True, label='')
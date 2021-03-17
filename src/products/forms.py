from django import forms

from .models import Product

class RawProductForm(forms.Form):
    title = forms.CharField(required=True, label ='')
    description = forms.CharField(required=False, label='', widget=forms.Textarea)
    price = forms.DecimalField(required=True, label='')
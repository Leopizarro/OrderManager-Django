from django import forms

from .models import Pedido

from django.forms import ModelForm

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        labels= {
            "motorista_id": "Selecciona el motorista de tu zona ! ->"
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comprador_id'].widget = forms.HiddenInput()
        self.fields['product_id'].widget = forms.HiddenInput()
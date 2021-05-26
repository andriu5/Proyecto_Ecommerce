from django import forms
from .models import *

class formProducto(forms.ModelForm):
    #nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Producto
        #fields = "__all__"
        fields = ["nombre","precio","categoria","inventario","descripcion","imagen"]
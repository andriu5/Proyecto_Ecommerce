from django import forms
from .models import Usuario

class UsuarioFormLogin(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ["email", "password"]


class UsuarioForm(forms.ModelForm):

    confirmPassword = forms.CharField(max_length=45, label ="Confirmar Password")
    
    class Meta:
        model = Usuario
        fields = ["nombre", "apellido", "email", "password"]
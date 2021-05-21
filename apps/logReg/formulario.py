from django import forms
from .models import User

class UsuarioFormLogin(forms.ModelForm):

    class Meta:
        model = User
        fields = ["email", "password"]


class UsuarioForm(forms.ModelForm):

    confirmPassword = forms.CharField(max_length=45, label ="Confirmar Password")
    confirmPassword.widget = forms.TextInput(
        attrs= {
            "placeholder": "Confirmar Password",
            "type": "password" 
        }
    )
    class Meta:
        model = User
        fields = ["nombre", "apellido", "email", "password"]
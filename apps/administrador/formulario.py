from django import forms
from apps.logReg.models import User

class AdminFormLogin(forms.ModelForm):

    Password = forms.CharField(max_length=45, label ="Ingresar Password")
    Password.widget = forms.TextInput(
        attrs= {
            "placeholder": "Ingresar Password",
            "type": "password" 
        }
    )
    class Meta:
        model = User
        fields = ["email", "password"]
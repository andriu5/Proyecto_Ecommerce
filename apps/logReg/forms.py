from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class EditPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=255, label ="Contraseña Actual")
    old_password.widget = forms.TextInput(
        attrs= {
            "placeholder": "Contraseña",
            "type": "password",
            "class":"form-control"
        }
    )
    new_password1 = forms.CharField(max_length=255, label ="Nueva Contraseña", help_text='<div class="form-text text-muted"><small>La contraseña debe cumplir los siguientes criterios:<ul><li>Su contraseña no puede ser muy similar a su otra información personal.</li><li>Su contraseña debe contener al menos 8 caracteres.</li><li>Su contraseña no puede ser una contraseña de uso común.</li><li>Tu contraseña no puede ser completamente numérica.</li></ul></small></div>')
    new_password1.widget = forms.TextInput(
        attrs= {
            "placeholder": "Contraseña",
            "type": "password",
            "class":"form-control"
        }
    )
    new_password2 = forms.CharField(max_length=255, label ="Confirmar nueva contraseña")
    new_password2.widget = forms.TextInput(
        attrs= {
            "placeholder": "Contraseña",
            "type": "password",
            "class":"form-control"
        }
    )
    class Meta:
        model = User
        fields = "__all__"

class EditProfileForm(UserChangeForm):
    password = forms.CharField(widget = forms.TextInput(attrs={"type": "hidden"}))
    username = forms.CharField(max_length=100, help_text = '<div class="form-text text-muted"><small>Campo Requerido. 100 caracteres o menos de Letras, digitos y los siguientes caracteres @/./+/-/_</small></div>')
    username.widget = forms.TextInput(
        attrs= {
            "placeholder": "Nombre de Usuario",
            "type": "text",
            "class":"form-control",
        }
    )
    email = forms.EmailField(required=True)
    email.widget = forms.TextInput(
        attrs= {
            "placeholder": "correo Electronico",
            "type": "email",
            "class":"form-control"
        }
    )
    first_name = forms.CharField(max_length=100, label ="Nombre")
    first_name.widget = forms.TextInput(
        attrs= {
            "placeholder": "Nombre",
            "type": "text",
            "class":"form-control"
        }
    )
    last_name = forms.CharField(max_length=100, label ="Apellido")
    last_name.widget = forms.TextInput(
        attrs= {
            "placeholder": "Apellido",
            "type": "text",
            "class":"form-control"
        }
    )
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")
        # fields = "__all__"

#Formulario de Registro de Usuarios
class NewUserForm(UserCreationForm):
    username = forms.CharField(max_length=100, help_text = '<div class="form-text text-muted"><small>Campo Requerido. 100 caracteres o menos de Letras, digitos y los siguientes caracteres @/./+/-/_</small></div>')
    username.widget = forms.TextInput(
        attrs= {
            "placeholder": "Nombre de Usuario",
            "type": "text",
            "class":"form-control",
        }
    )
    email = forms.EmailField(required=True)
    email.widget = forms.TextInput(
        attrs= {
            "placeholder": "correo Electronico",
            "type": "email",
            "class":"form-control"
        }
    )
    first_name = forms.CharField(max_length=100, label ="Nombre")
    first_name.widget = forms.TextInput(
        attrs= {
            "placeholder": "Nombre",
            "type": "text",
            "class":"form-control"
        }
    )
    last_name = forms.CharField(max_length=100, label ="Apellido")
    last_name.widget = forms.TextInput(
        attrs= {
            "placeholder": "Apellido",
            "type": "text",
            "class":"form-control"
        }
    )
    password1 = forms.CharField(max_length=255, label ="Contraseña", help_text='<div class="form-text text-muted"><small>La contraseña debe cumplir los siguientes criterios:<ul><li>Su contraseña no puede ser muy similar a su otra información personal.</li><li>Su contraseña debe contener al menos 8 caracteres.</li><li>Su contraseña no puede ser una contraseña de uso común.</li><li>Tu contraseña no puede ser completamente numérica.</li></ul></small></div>')
    password1.widget = forms.TextInput(
        attrs= {
            "placeholder": "Contraseña",
            "type": "password",
            "class":"form-control"
        }
    )
    password2 = forms.CharField(max_length=255, label ="Confirmar Contraseña", help_text = '<div class="form-text text-muted"><small>Campo Requerido. Ingrese la misma contraseña.</small></div>')
    password2.widget = forms.TextInput(
        attrs= {
            "placeholder": "Confirmar Contraseña",
            "type": "password",
            "class":"form-control"
        }
    )
    # fav_color = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2",)


#Formulario de Inicio de Sesion
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ["email", "password"]
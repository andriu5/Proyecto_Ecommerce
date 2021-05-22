from django import forms
from apps.logReg.models import User

class AdminFormLogin(forms.ModelForm):

    class Meta:
        model = User
        fields = ["email", "password"]
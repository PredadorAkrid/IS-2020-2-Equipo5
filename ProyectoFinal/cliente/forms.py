# Django
from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class RegistroCliente(forms.Form):
    """Sign up new user form."""
    

    nombre = forms.CharField(max_length=64)
    paterno = forms.CharField(max_length=100)
    materno = forms.CharField(max_length=100, required=False )
    correo = forms.EmailField(max_length=254)
    contrasenia = forms.CharField(max_length=16)
    telefono = forms.CharField(max_length=10)
   
    def clean_correo(self):
        """Validate that the email doesn't exist in the database."""
        data = self.cleaned_data["correo"]
        if User.objects.filter(email=data).count() > 0:
            raise forms.ValidationError("Éste correo ya está registrado")

        return data
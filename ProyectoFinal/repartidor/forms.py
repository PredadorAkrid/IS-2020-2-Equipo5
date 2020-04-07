"""Formularios Repartidor"""
#Django
from .models import *
from django import forms
from django.contrib.auth.models import *
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm















'''
class RegistrarRepartidor(forms.Form):

	nombre = forms.CharField(max_length=64)
    paterno = forms.CharField(max_length=100)
    materno = forms.CharField(max_length=100, required=False)
    correo = forms.EmailField(max_length=254)

	def clean_correo(self):
		"""Valida que el correo no exista en la base de datos"""
		data = self.cleaned_data["correo"]
		if Repartidor.objects.filter(correo_repartidor=data).count() > 0:
			raise forms.ValidationError("Este correo ya existe para un repartidor")

		return data
'''

from django import forms
from django.contrib.auth.models import User
from .models import *
#Formulario para crear las categorías
class CategoriaForm(forms.ModelForm):
	nombre_categoria =  forms.CharField(required=True,  max_length = 100, label='Nombre Categoria'),
	class Meta:
		model = Categoria
		fields = [
			'nombre_categoria',
		]

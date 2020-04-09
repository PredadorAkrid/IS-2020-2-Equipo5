""" Formularios para platillos """

from django import forms
from .models import Platillo
from django.contrib.auth.models import User


class FormularioCrearPlatillo(forms.ModelForm):
    """Formulario para crear un nuevo platillo"""
    nombre = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.FloatField()
    imagen = forms.FileField(required=False)

    class Meta:
        db_table = "platillo"
        model = Platillo
        fields = ("nombre", "descripcion", "precio", "imagen")

    def nombre_existente(self):
        """ Metodo para evitar nombres duplicados """
        nombre = self.clean_data["nombre"]
        if Platillo.objects.filter(nombre=nombre).count() > 0:
            raise forms.ValidationError("El nombre del platillo ya existe!")
        return nombre


class FormularioSeleccionPlatillo(forms.ModelForm):
    """Formulario para la seleccion del platillo"""
    seleccion = forms.ModelChoiceField(queryset=Platillo.objects.all())

    class Meta:
        db_table = "platillo"
        model = Platillo
        fields = ("seleccion",)


class FormularioEditarPlatillo(forms.ModelForm):
    """Formulario para editar un platillo"""
    nombre = forms.CharField(required=False)
    descripcion = forms.CharField(required=False)
    precio = forms.FloatField(required=False)
    imagen = forms.FileField(required=False)

    class Meta:
        db_table = "platillo"
        model = Platillo
        fields = ("nombre", "descripcion", "precio", "imagen")

    def nombre_existente(self):
        """ Metodo para evitar nombres duplicados """
        nombre = self.clean_data["nombre"]
        if Platillo.objects.filter(nombre=nombre).count() > 0:
            raise forms.ValidationError("El nombre del platillo ya existe!")
        return nombre

"""Repartidor configuración de URL."""
from django.contrib import admin
from django.urls import include, path

from repartidor import views

app_name = "repartidor"

urlpatterns = [

	#temporal, no se llamarán así las vistas
    path("", views.Index.as_view(), name="Index"),
	path('registrar_repartidor', views.RegistrarRepartidor.as_view(), name = 'registrar_repartidor'),


]

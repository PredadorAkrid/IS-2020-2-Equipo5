"""Repartidor configuración de URL."""
from django.contrib import admin
from django.urls import include, path

from repartidor import views

app_name = "repartidor"

urlpatterns = [

	#temporal, no se llamarán así las vistas
    path("repartidor", views.Index.as_view(), name="Index"),
    #path("top-songs", views.TopSongs.as_view(), name="top-songs"),

    #path("artist/create-artist", views.AddArtist.as_view(), name="add_artist"),


]

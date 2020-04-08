from django.urls import path
from django.conf.urls import url,include
app_name = "administrador"

from administrador import views
from .views import *

urlpatterns = [
    
	#temporal, no se llamarán así las vistas
   	path("", views.Index.as_view(), name="Index"),
    #path("top-songs", views.TopSongs.as_view(), name="top-songs"),
    path("editar-ordenes/", views.EditarOrdenes.as_view(), name="ordenes_administrador"),
    path("lista-ordenes/", lista_ordenes, name="listar_ordenes"),
    #path("artist/create-artist", views.AddArtist.as_view(), name="add_artist"),


]

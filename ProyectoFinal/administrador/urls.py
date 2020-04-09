from django.urls import path
from django.conf.urls import url, include

from administrador import views
from .views import *
app_name = "administrador"

urlpatterns = [
    
	#temporal, no se llamarán así las vistas
   	path("", views.Index.as_view(), name="Index"),
   	
    #path("editar-ordenes/", views.EditarOrdenes.as_view(), name="ordenes_administrador"),
    #path("lista-ordenes/", lista_ordenes, name="listar_ordenes"),
    path("lista-ordenes/", lista_ordenes, name="listar_ordenes"),
    path("editar-ordenes/(?P<pk>d+)/",editar_orden, name="editar_orden"),
    path("eliminar-ordenes/(?P<pk>d+)/",eliminar_orden, name="eliminar_orden"),
]

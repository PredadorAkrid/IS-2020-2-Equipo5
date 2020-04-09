from django.urls import path
from django.conf.urls import url, include
from .views import *

app_name = "categoria"

urlpatterns = [
	#temporal, no se llamarán así las vistas
   	path("", Index.as_view(), name="Index"),
   	path("crear-categoria", crear_categoria, name="crear_categoria"),
   	path("ver-categorias/", lista_categoria, name="listar_categorias")

]

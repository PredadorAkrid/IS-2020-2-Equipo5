from django.urls import path
from django.conf.urls import url,include
from .views import *
from cliente import views
app_name = "cliente"


urlpatterns = [
	#Vistas basadas en clases
	path("", views.Index.as_view(), name="IndexCliente"),
	#Registro de cliente
   	path("registro-cliente/", views.RegistroCliente.as_view(), name="registro_cliente"),
   	#Inicio de sesión de clientes y repartidores
   	#path("iniciar-sesion/", views.InicioSesion.as_view(), name="inicio_sesion"),
   	#Cerrar sesión para clientes y repartidores
   	path("cerrar-sesion/", views.CerrarSesion.as_view(), name="cerrar_sesion"),


]

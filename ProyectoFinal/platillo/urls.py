from django.urls import path
from . import views

urlpatterns = [
    # Vistas de clase
    path('platillos', views.Index.as_view(), name='platillos'),
    path('platillos/crear', views.CrearPlatillo.as_view(), name="crear_platillo"),
    path('platillos/seleccionar', views.SeleccionarPlatillo.as_view(),
         name="seleccionar"),
    path('platillos/editar',
         views.EditarPlatillo.as_view(), name="editar"),
    path('platillos/eliminar', views.EliminarPlatillo.as_view(), name="eliminar"),
    path('platillos/ver', views.VerPlatillos.as_view(), name="ver"),
]

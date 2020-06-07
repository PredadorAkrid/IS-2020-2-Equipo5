from django.urls import path, re_path
from django.conf.urls import url, include
from .views import *
from cliente import views
from .models import *
app_name = "cliente"

# Url's para cliente
urlpatterns = [
    # Vistas basadas en clases
    path("", views.Index.as_view(), name="IndexCliente"),
    path("home/", HomeCliente, name="HomeCliente"),

    # Registro de cliente
    path("registro-cliente/", views.RegistroCliente.as_view(),
         name="registro_cliente"),
    # Inicio de sesión de clientes y repartidores
    #path("iniciar-sesion/", views.InicioSesion.as_view(), name="inicio_sesion"),
    # Cerrar sesión para clientes y repartidores
    path("cerrar-sesion/", views.CerrarSesion.as_view(), name="cerrar_sesion"),
    path("carrito/", CarritoView, name="carrito"),
    path('cart/add/<int:pk>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:pk>/', views.item_clear, name='item_clear'),
    path('cart/item_clear/confirmar/', views.confirmar, name='confirmar'),
    path('ver_menu/', views.ver_menu, name="ver_menu"),


    # path('cart/item_increment/<int:id>/',
    #     views.item_increment, name='item_increment'),
    # path('cart/item_decrement/<int:id>/',
    #     views.item_decrement, name='item_decrement'),
    #path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    # path('cart/cart-detail/',views.cart_detail,name='cart_detail'),


]

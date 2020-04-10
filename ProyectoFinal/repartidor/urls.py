from django.conf.urls import url,include
from django.urls import path
from . import views
from .views import *

app_name = "repartidor"

urlpatterns = [
    path("repartidor/", views.IndexRepartidor.as_view(), name="IndexRepartidor"),
    path("registro-repartidor/", views.RegistroRepartidor.as_view(), name="registro-repartidor"),
    path("ordenes-para-recoleccion/", ordenes_para_recoleccion, name="ordenes-para-recoleccion"),
]

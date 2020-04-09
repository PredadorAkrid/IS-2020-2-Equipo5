from django.urls import path
from django.conf.urls import url,include
from .views import *
from repartidor import views


app_name = "repartidor"

urlpatterns = [
    
	
    path("repartidor", views.IndexRepartidor.as_view(), name="IndexRepartidor"),
    


]

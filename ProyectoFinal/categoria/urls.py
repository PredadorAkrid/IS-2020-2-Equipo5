from django.urls import path
from django.conf.urls import url, include

from .views import *
from categoria import views
app_name = "categoria"

urlpatterns = [

	#temporal, no se llamarán así las vistas
   	path("", views.Index.as_view(), name="Index"),
]

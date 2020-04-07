from django.urls import path
from django.conf.urls import url,include
from .views import *
from repartidor import views


app_name = "repartidor"

urlpatterns = [
    
	#temporal, no se llamarán así las vistas
    path("repartidor", views.IndexRepartidor.as_view(), name="IndexRepartidor"),
    #path("top-songs", views.TopSongs.as_view(), name="top-songs"),
    
    #path("artist/create-artist", views.AddArtist.as_view(), name="add_artist"),


]

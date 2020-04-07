from django.urls import path
from . import views

urlpatterns = [
    # Vistas de clase
    path('platillos', views.Index.as_view(), name='platillo'),
]

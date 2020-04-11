from django.contrib import admin
from .models import Platillo

<<<<<<< HEAD
=======

>>>>>>> origin/Lechuga
class AdministradorPlatillos(admin.ModelAdmin):
    """Clase especial para que muestre el id de los platillos"""
    list_display = ("id", "nombre", "descripcion", "precio", "imagen")


# Register your models here.
<<<<<<< HEAD
admin.site.register(Platillo, AdministradorPlatillos)
=======
admin.site.register(Platillo, AdministradorPlatillos)
>>>>>>> origin/Lechuga

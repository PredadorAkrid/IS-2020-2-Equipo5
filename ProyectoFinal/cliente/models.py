from django.db import models

# Create your models here.
class Cliente(models.Model):
    """Artist Model."""
    # campo nombre
    id_cliente = models.AutoField(primary_key=True, db_column='id_cliente')
    nombre_cliente = models.CharField(max_length=64)
    apellido_pa_cliente = models.CharField(max_length=100)
    apellido_ma_cliente = models.CharField(max_length=100)
    correo_cliente = models.EmailField(max_length=254)
    contra_cliente = models.CharField(max_length=16)
    telefono_cliente = models.CharField(max_length=10) 

    # Representación en cadena de un objeto artista
	    class Meta:
	        db_table = 'cliente'
class Direccion(models.Model):
	id_direccion = models.IntegerField(primary_key=True)
	id_cliente =  models.ForeignKey(Person, models.DO_NOTHING)
	descripcion_direccion = models.CharField(max_length=200)
	class Meta:
        db_table = 'direccion'
        unique_together = (('id_cliente', 'descripcion_direccion' ),)




    
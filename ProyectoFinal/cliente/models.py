from django.db import models
from django.contrib.auth.models import User
from platillo.models import *

#Tabla cliente para guardar los clientes de la aplicación
class Cliente(models.Model):
    user_cliente = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    id_cliente = models.AutoField(primary_key=True, db_column='id_cliente')
    nombre_cliente = models.CharField(max_length=64)
    apellido_pa_cliente = models.CharField(max_length=100)
    apellido_ma_cliente = models.CharField(max_length=100)
    telefono_cliente = models.CharField(max_length=10) 
    def __str__(self):
        return str(self.user_cliente)
    #Definimos el nombre de la tabla y el nombre en plural para el panel de administador
    class Meta:
        db_table = 'cliente'
        verbose_name_plural = "Clientes"           
#Tabla auxiliar para tener el atributo multivaluado de dirección de un cliente

class Direccion(models.Model):
    id_direccion = models.IntegerField(primary_key=True)
    id_cliente =  models.ForeignKey(Cliente, models.DO_NOTHING)
    descripcion_direccion = models.CharField(max_length=200)
    class Meta:
        db_table = 'direccion'
        verbose_name_plural = "Direcciones"
        unique_together = (('id_cliente', 'descripcion_direccion' ))
    def __str__(self):
        return '{}'.format(self.descripcion_direccion)

class Carrito(models.Model):
    id_platillo_carrito = models.IntegerField(primary_key=True,null=False),
    id_cliente_carrito =models.IntegerField(primary_key=True,null=False),
    cantidad_carrito = models.IntegerField(null=False, default = 0),
    precio_platillo_carrito = models.IntegerField(null=False, default = 0),
    
    class Meta:
        db_table = 'carrito'
        verbose_name_plural = "Carritos"
    
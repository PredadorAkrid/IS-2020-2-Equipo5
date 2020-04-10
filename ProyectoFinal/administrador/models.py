from django.db import models
#from cliente.models import *
from cliente import models
from repartidor  import models
from platillo import  models
from repartidor.models import *
from cliente.models import *
# Create your models here.

class Orden(models.Model):
	id_orden = models.AutoField(primary_key=True)
	precio_orden = models.IntegerField(null=False, default = 0)
	id_cliente_orden = models.ForeignKey('cliente.Cliente', on_delete=models.SET_DEFAULT, default=0)
	id_repartidor_orden = models.ForeignKey('repartidor.Repartidor',on_delete= models.SET_NULL, blank =True,  null=True)
	id_platillo_orden  = models.ManyToManyField('platillo.Platillo', null=True)
	id_estado_orden =    models.ForeignKey('EstadoOrden',  on_delete=models.SET_DEFAULT, default=0)
	direccion_entrega_orden  = models.ForeignKey('cliente.Direccion', null=False, on_delete=models.CASCADE)
	class Meta:
		db_table = 'orden'
		verbose_name_plural = "Ordenes"
class EstadoOrden(models.Model):
	"""docstring for EstadoOrden"""
	id_estado = models.IntegerField(primary_key=True)
	descripcion_estado = models.CharField(max_length=30)
	class Meta:
		db_table = 'estado_orden'
		verbose_name_plural = "EstadosOrden"
	def __str__(self):
		return '{}'.format(self.id_estado)

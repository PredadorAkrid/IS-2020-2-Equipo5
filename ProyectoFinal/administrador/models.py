from django.db import models
#from cliente.models import *
from cliente import models
from repartidor  import models
from platillo import  models
from repartidor.models import *
# Create your models here.

class Orden(models.Model):
	id_orden = models.AutoField(primary_key=True)
	precio_orden = models.IntegerField(null=False, default = 0)
	id_cliente = models.ForeignKey('cliente.Cliente', on_delete=models.SET_DEFAULT, default=0)
	id_repartidor = models.ForeignKey('repartidor.Repartidor',on_delete= models.SET_DEFAULT, null=True, default = 0)
	id_platillo  = models.ManyToManyField('platillo.Platillo', null=True)
	id_estado =    models.ForeignKey('EstadoOrden',  on_delete=models.SET_DEFAULT, default=0)
	direccion_entrega  = models.CharField(null=False, max_length=200)
	#estado_orden = models.VarChar()

class EstadoOrden(models.Model):
	"""docstring for EstadoOrden"""
	id_estado = models.IntegerField(primary_key=True)

	descripcion_estado = models.CharField(max_length=30)

	def __init__(self, arg):
		super(EstadoOrden, self).__init__()
		self.arg = arg

from django.db import models
from cliente import models as cliente_models
from repartidor  import models as repartidor_models
# Create your models here.


#class Orden(models.Model):
#	id_orden = models.AutoField(primary_key=True)
#	precio_orden = models.IntegerField(null=False, default = 0)
#	id_cliente = models.ForeignKey('cliente_models.Cliente')
#	id_repartidor = models.ForeignKey('repartidor_models.Repartidor')
#	id_platillo  = models.ManyToManyField('Platillo', related_name='platillos')
#	direccion_entrega  = models.CharField(null=false, max_length=200)

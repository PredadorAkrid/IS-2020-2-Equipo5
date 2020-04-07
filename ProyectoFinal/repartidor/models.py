"""Modelos Repartidor"""
#Django
from django.db import models

class Repartidor(models.Model):
	"""Modelo Repartidor"""

	id_repatidor = models.AutoField(primary_key=True, db_column='id_repatidor')
	nombre_repartidor = models.CharField(max_length=64)
	apellido_paterno_repartidor = models.CharField(max_length=100)
	apellido_materno_repartidor = models.CharField(max_length=100)
	correo_repartidor = models.EmailField(max_length=254)
	password_repartidor = models.CharField(max_length=16)

	def __str__(self):
		return self.nombre_repartidor + " " + self.apellido_paterno_repartidor

	def __repr__(self):
		"""Representación en cadena de un Repartidor"""
		return self.__str__()

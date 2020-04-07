"""Modelos Repartidor"""
#Django
from django.db import models
from django.contrib.auth.models import User

'''

class Repartidor(models.Model):
	"""Modelo Repartidor"""

	id_repatidor = models.AutoField(primary_key=True, db_column='id_repatidor')
	nombre_repartidor = models.CharField(max_length=64)
	apellido_paterno_repartidor = models.CharField(max_length=100)
	apellido_materno_repartidor = models.CharField(max_length=100)
	correo_repartidor = models.EmailField(max_length=254)
	password_repartidor = models.CharField(max_length=16, null=True)

	def __str__(self):
		return self.nombre_repartidor + " " + self.apellido_paterno_repartidor

	def __repr__(self):
		"""Get str representation"""
		return self.__str__()

'''
class Repartidor(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
	id_repatidor = models.AutoField(primary_key=True, db_column='id_repatidor')
	nombre_repartidor = models.CharField(max_length=64)
	apellido_paterno_repartidor = models.CharField(max_length=100)
	apellido_materno_repartidor = models.CharField(max_length=100)
	correo_repartidor = models.EmailField(max_length=254)

	def __str__(self):
		return self.nombre_repartidor + " " + self.apellido_paterno_repartidor
	class Meta:
		db_table = 'repartidor'

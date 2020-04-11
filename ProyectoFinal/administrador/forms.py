from django import forms
from .models import *


'''Descontinuado 
class AdminForm(forms.ModelForm):
   	usuario = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:

        widgets = {
      	    'password': forms.PasswordInput()
        }
'''



'''
Formulario para editar las órdenes existentes como administrador
'''

class OrdenForm(forms.ModelForm):
	precio_orden =  forms.IntegerField(required=True, label='Precio'),
	id_cliente_orden =  forms.IntegerField(required=True, label='Cliente'),
	id_repartidor_orden =  forms.IntegerField(required=False, label='Repartidor asignado'),
	id_estado_orden = forms.IntegerField(required=True, max_value=5, min_value=1, label='Estado entrega'),
	id_platillo_orden =  forms.MultipleChoiceField(required=True, label='Platillos'),
	direccion_entrega_orden = forms.CharField(required=True, label='Direccion')
	class Meta:
		#Indicamos el modelo
		model = Orden
		#Los campos del modelo
		fields = [
			'precio_orden',
			'id_cliente_orden',
			'id_repartidor_orden',
			'id_estado_orden',
			'id_platillo_orden',
			'direccion_entrega_orden',
		]			
		#Etiquetas pero no funcionan, se puede borrar
		labels = {
			'precio_orden':'Precio final',
			'id_cliente_orden':'Cliente',
			'id_repartidor_orden':'Repartidor asignado',
			'id_estado_orden':'Estado Orden',
			'id_platillo_orden':'Platillos',
			'direccion_entrega_orden':'Direccion entrega',
		}
		
	
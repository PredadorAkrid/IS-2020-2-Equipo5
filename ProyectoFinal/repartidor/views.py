"""Vistas Repartidor"""
#Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import *
from django.http import HttpResponse
from django.views import View
#Models
from .models import Repartidor
# Forms
from repartidor.forms import *

# Create your views here.

##Class-based-views
class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        return HttpResponseForbidden()


class RegistrarRepartidor(View):
	"""Registrar un nuevo repartidor"""

	template = "repartidor/registrar-repartidor.html"

	def get(self, request):
		form = RegistrarRepartidorFormulario()
		context = {"form" : form}
		return render(request, self.template, context)

	def post(self, request):
		form = RegistrarRepartidorFormulario(request.POST, request.FILES)
		if not form.is_valid():
			context = {"form" : form}
			return render(request, self.template, context)

		Repartidor.objects.create(
			nombre_repartidor = form.cleaned_data["nombre"],
			apellido_paterno_repartidor = form.cleaned_data["paterno"],
			apellido_materno_repartidor = form.cleaned_data["materno"],
			correo_repartidor = form.cleaned_data["correo"],
			password_repartidor = form.cleaned_data["password"],
		)

		#return render(request, "repartidor/index.html")
		return HttpResponse("<h1>Repartidor registrado!</h1>")

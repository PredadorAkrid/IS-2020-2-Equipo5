
from django.shortcuts import render
from django.views import View

# Create your views here.
##Function based views

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse

from .models import *
from .forms import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
def superuser_only(function):
    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return _inner

#Vista basada en funciones para el index de administrador
@login_required
@superuser_only
def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        return HttpResponseForbidden()

#Función para listar las órdenes registradas
#@staff_member_required
@login_required
@superuser_only
def lista_ordenes(request):
	ordenes = Orden.objects.all().order_by('id_orden')
	contexto = {'ordenes': ordenes}
	return render(request, 'administrador/lista_ordenes.html',contexto)


#Función para editar una orden en particular
#@staff_member_required
@login_required
@superuser_only
def editar_orden(request,  pk):
	orden_a_editar = Orden.objects.get(id_orden= pk)
	if request.method == 'GET':
		form = OrdenForm(instance=orden_a_editar)
	elif request.method == 'POST':
		form = OrdenForm(request.POST, instance=orden_a_editar)
		if form.is_valid():
			form.save()
		return redirect('administrador:lista_ordenes')
	return render(request, 'administrador/ordenes.html', {'form':form})





#Función para eliminar una orden
#@user_passes_test(lambda u: u.is_superuser)
@login_required
@superuser_only
def eliminar_orden(request,  pk):
	orden_a_editar = Orden.objects.get(id_orden= pk)
	if request.method == 'POST':
		orden_a_editar.delete()
		return redirect('administrador:listar_ordenes')
	#Cargamos el html para la confirmación de eliminar la orden
	return render(request, 'administrador/eliminar_orden.html', {'orden':orden_a_editar})

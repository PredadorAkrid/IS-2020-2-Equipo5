
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
##Class-based-views

class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        return HttpResponseForbidden()

def lista_ordenes(request):
	ordenes = Orden.objects.all().order_by('id_orden')
	contexto = {'ordenes': ordenes}
	return render(request, 'administrador/lista_ordenes.html',contexto)



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

def eliminar_orden(request,  pk):
	orden_a_editar = Orden.objects.get(id_orden= pk)
	if request.method == 'POST':
		orden_a_editar.delete()
		return redirect('administrador:listar_ordenes')
	return render(request, 'administrador/eliminar_orden.html', {'orden':orden_a_editar})




'''NO ME SIRVIO
class OrdenList(ListView):
	model = Orden
	template_name = 'administrador/lista_ordenes.html'
	paginate_by = 2

def lista_ordenes(request):
	ordenes = Orden.objects.all().order_by('id_orden')
	contexto = {'ordenes': ordenes}
	return render(request, 'administrador/lista_ordenes.html',contexto)

class EditarOrdenes(UpdateView):
	model = Orden
	form_class = OrdenForm
	template_name = 'administrador/ordenes.html'

'''

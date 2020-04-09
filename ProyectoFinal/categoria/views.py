from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Categoria
from .forms import *
# Create your views here.

class Index(View):
    def get(self, request):
        return render(request, 'categoria/index.html')
    def post(self, request):
        return HttpResponseForbidden()

def crear_categoria(request):
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('administrador:Index')
	elif request.method == 'GET':
		form = CategoriaForm()
		context = {"form": form}
		return render(request, 'categoria/crear_categoria.html', context)  
def lista_categoria(request):
	categorias = Categoria.objects.all().order_by('nombre_categoria')
	print(categorias)
	contexto = {'categorias': categorias}
	return render(request, 'categoria/lista_categorias.html',contexto)

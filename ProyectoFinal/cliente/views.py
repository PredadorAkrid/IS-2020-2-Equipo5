from django.shortcuts import render
from django.views import View

# Create your views here.
##Function based views

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout
from .forms import *


# Create your views here.

class RegistroCliente(View):
    """New User Sign Up."""
    def get(self, request):
        """Render sign up form."""
        form = SignUpForm()
        print(form)
        context = {"form": form}
        return render(request, 'cliente/registro_cliente.html', context)  
    def post(self, request):
        form = SignUpForm(request.POST)
        if not form.is_valid():
            context = {"form": form}
            return render(request, 'cliente/registro_cliente.html', context)
        
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        user2 = Cliente.objects.create_user(
            user_cliente = user,
		    nombre_cliente =form.cleaned_data["nombre"],
		    apellido_pa_cliente = form.cleaned_data["paterno"],
		    apellido_ma_cliente = form.cleaned_data["materno"],
		    telefono_cliente = form.cleaned_data["telefono"],
        )
        user2.save()
        return HttpResponse("<h1>Cliente creado</h1>")

class Index(View):
    def get(self, request):
        return render(request, 'cliente/index.html')
    def post(self, request):
        return HttpResponseForbidden()
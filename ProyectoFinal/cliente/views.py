from django.shortcuts import render
from django.views import View

# Create your views here.

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
        form = ClienteRegistroForm()
        context = {"form": form}
        return render(request, 'cliente/registro_cliente.html', context)
    def post(self, request):
        form = SignUpForm(request.POST)
        if not form.is_valid():
            context = {"form": form}
            return render(request, 'cliente/registro_cliente.html', context)
        print("es valido")
        user = form.save(commit=False)
        user.is_active = True
        user.save()

        user2 = Cliente(
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
        form = InicioSesionForm()
        context = {"form": form}
        return render(request, "cliente/index.html", context)
    def post(self, request):

        """Receive and validate sign up form."""
        form = InicioSesionForm(data=request.POST)
        if not form.is_valid():
            print("no es válido")
            context = {"form": form}
            return render(request, "cliente/index.html", context)

        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        # As simple as telling django the user to login.
        login(request, user)

        return HttpResponse("<h1>Usuario logeado!</h1>")

'''
class InicioSesion(View):
    """Cliente Inicio Sesión."""
    def get(self, request):
        """Render sign up form."""
        form = InicioSesionForm()
        context = {"form": form}
        return render(request, "cliente/index.html", context)
    def post(self, request):

        """Receive and validate sign up form."""
        form = InicioSesionForm(data=request.POST)
        if not form.is_valid():
            context = {"form": form}
            return render(request, "cliente/index.html", context)

        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        # As simple as telling django the user to login.
        login(request, user)

        return HttpResponse("<h1>User logged!</h1>")

'''
class CerrarSesion(View):
    def get(self, request):
        logout(request)
        return redirect("cliente:IndexCliente")

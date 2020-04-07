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
        print("es valido")
        user = form.save(commit=False)
        user.is_active = False
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
        return render(request, 'cliente/index.html')
    def post(self, request):
        return HttpResponseForbidden()

class InicioSesion(View):
    """Cliente Inicio Sesión."""
    def get(self, request):
        """Render sign up form."""
        form = InicioSesionForm()
        context = {"form": form}
        return render(request, "cliente/login.html", context)
    def post(self, request):

        """Receive and validate sign up form."""
        form = LoginForm(data=request.POST)
        if not form.is_valid():
            context = {"form": form}
            return render(request, self.template, context)
        user = authenticate(
            username=form.cleaned_data["usuario"],
            password=form.cleaned_data["clave"],
        )
        # As simple as telling django the user to login.
        login(request, user)

        return HttpResponse("<h1>User logged!</h1>")
    '''
    def post(self, request):
        """Receive and validate sign up form."""
        form = LoginForm(data=request.POST)

        if not form.is_valid():
            context = {"form": form}
            return render(request, self.template, context)

        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        # As simple as telling django the user to login.
        login(request, user)

        return redirect("music:home")

    '''
class LogoutView(View):
    """Logout View."""

    def get(self, request):
        """Logout logged user."""
        # As simple as.
        logout(request)
        return redirect("music:home")

"""Vistas Repartidor"""
#Django
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib.auth.models import *
from django.http import HttpResponse
from django.views import View
from .forms import *

class IndexRepartidor(View):
    """Pagina Index para los platillos"""

    template = "repartidor/index.html"

    def get(self, request):
        print("llega a repartidores")
        """Metodo Get"""
        return render(request, self.template)

class RegistroRepartidor(View):
    """Registro nuevo repartidor"""

    template = "repartidor/registro-repartidor.html"

    def get(self, request):
        """Render sign up form"""

        form = FormularioRegistroRepartidor()
        context = {"form" : form}
        return render(request, self.template, context)

    def post(self, request):
        form = FormularioRegistroRepartidor(request.POST)
        if not form.is_valid():
            context = {"form": form}
            return render(request, self.template, context)
        print("El form es válido")

        user = form.save(commit=False)
        user.is_active = False
        user.save()

        userRepartidor = Repartidor(
            user = user,
            nombre_repartidor = form.cleaned_data["nombre"],
            apellido_paterno_repartidor = form.cleaned_data["paterno"],
            apellido_materno_repartidor = form.cleaned_data["materno"],
        )

        userRepartidor.save()

        mail_subject = "Registro existoso | Delivery&Eats"
        mail_message = render_to_string("repartidor/registro-repartidor-email.html",{
            'user' : user,
        })
        to_email = form.cleaned_data['email']
        email = EmailMessage(mail_subject, mail_message, to=[to_email])
        email.send()

        return HttpResponse("<h1>Repartidor registrado</h1>")

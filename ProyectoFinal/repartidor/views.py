"""Vistas Repartidor"""
#Django
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib.auth.models import *
from django.http import HttpResponse
from django.views import View
from .forms import *
from administrador.models import Orden, EstadoOrden

class IndexRepartidor(View):
    """Pagina Index para los repartidores"""

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

        data = form.save(commit=False)
        user = data["user"]
        cont = data["cont"]
        user.is_active = False
        user.is_staff = True
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
            'user' : userRepartidor,
            'password': cont
        })
        to_email = form.cleaned_data['email']
        email = EmailMessage(mail_subject, mail_message, to=[to_email])
        email.send()

        return HttpResponse("<h1>Repartidor registrado</h1>")

# Función que despliega la lista de ordenes listas para recolección
@staff_member_required
def ordenes_para_recoleccion(request):
    ordenes_recoleccion = Orden.objects.filter(id_estado_orden=3).order_by('id_orden')
    contexto = {'ordenes' : ordenes_recoleccion}
    return render(request, "repartidor/ordenes_para_recoleccion.html", contexto)

#Funcion que despliega las ordenes asignadas a un repartidor
@staff_member_required
def ordenes_asignadas(request):
    repartidor = Repartidor.objects.get(user=request.user)
    ordenes_asignadas = Orden.objects.filter(id_repartidor_orden=repartidor).order_by('id_orden')
    contexto = {'ordenes' : ordenes_asignadas}
    return render(request, "repartidor/ordenes_asignadas.html", contexto)

#Función que permite a un repartidor seleccionar una orden y comenzar su entrega.
#Cambia el estado de la orden a "4: Pedido recolectado"
#Asigna al repartidor a la orden
@staff_member_required
def comenzar_entrega(request, pk):
    orden_por_entregar = Orden.objects.get(id_orden=pk)
    repartidor = Repartidor.objects.get(user=request.user)
    estado = EstadoOrden.objects.get(id_estado=4)

    orden_por_entregar.id_estado_orden = estado
    orden_por_entregar.id_repartidor_orden = repartidor
    orden_por_entregar.save()
    return redirect('repartidor:ordenes_asignadas')

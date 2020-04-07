"""Vistas Repartidor"""
#Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout
class IndexRepartidor(View):
    """Pagina Index para los platillos"""

    template = "repartidor/index.html"

    def get(self, request):
        print("llega a repartidores")
        """Metodo Get"""
        return render(request, self.template)

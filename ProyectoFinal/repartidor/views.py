"""Vistas Repartidor"""
#Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout
from cliente import views
class Index(View):
    """Pagina Index para los platillos"""

    template = "repartidor/index.html"

    def get(self, request):
        """Metodo Get"""
        return render(request, self.template)

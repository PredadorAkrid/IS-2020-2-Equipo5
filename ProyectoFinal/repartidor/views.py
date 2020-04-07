from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View

# Create your views here.
##Function based views

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout
class IndexRepartidor(View):
    """Pagina Index para los platillos"""

    template = "repartidor/index.html"

    def get(self, request):
        print("llega a repartidores")
        """Metodo Get"""
        return render(request, self.template)
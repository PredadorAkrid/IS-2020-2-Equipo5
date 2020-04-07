# Django
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.


class Index(View):
    """Pagina Index para los platillos"""

    template = "platillo/index.html"

    def get(self, request):
        """Metodo Get"""
        return render(request, self.template)

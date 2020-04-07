from django.shortcuts import render
from django.views import View

# Create your views here.

class Index(View):
    """Pagina Index para los platillos"""

    template = "platillo/index.html"

    def get(self, request):
        """Metodo Get"""
        return render(request, self.template)
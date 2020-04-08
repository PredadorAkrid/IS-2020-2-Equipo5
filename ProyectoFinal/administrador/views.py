
from django.shortcuts import render
from django.views import View

# Create your views here.
##Function based views

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout


from .models import *
from .forms import *
##Class-based-views

class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        return HttpResponseForbidden()

class EditarOrdenes(View):
    def get(self,request):
    	'''
        ordenes = Orden.objects.all()
        context = {"ordenes": ordenes}

        
        #books= zip(ID, bookName, author, copies)
        return render(request, 'administrador/ordenes.html', context)
 		#return render(request, 'allbooks.html',{ "books": books} )
    	'''
    	#form = OrdenForm()
    	return render(request,'administrador/ordenes.html', {'form':form} )
    def post(self,request):
        #aquí hay
        form = OrdenForm(request.POST)
        if form.is_valid():
        	form.save()
        return redirect('orden:Index')	

def lista_ordenes(request):
	ordenes = Orden.objects.all().order_by('id_orden')
	contexto = {'ordenes': ordenes}
	return render(request, 'administrador/lista_ordenes.html',contexto)



'''
class EditarOrden(self, request, id):
	orden = Orden.objects.get(id_orden = id)
	def get(self, request):
		form = OrdenForm(instance = mascota)	
	def post(self, request):
		pass
'''

'''
Forma 1:

from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def foo_view(request):

Forma 2:
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def foo_view(request):
   if not request.user.is_superuser:
       return HttpResponse('The user is not superuser')
'''
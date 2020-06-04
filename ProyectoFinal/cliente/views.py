from django.shortcuts import render
from django.views import View

# Create your views here.

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import * 
from repartidor.models import * 
# Create your views here.
from django.contrib.auth.decorators import login_required

class RegistroCliente(View):
    """New User Sign Up."""
    def get(self, request):
        """Render sign up form."""
        form = ClienteRegistroForm()
        context = {"form": form}
        return render(request, 'cliente/registro_cliente.html', context)  
    def post(self, request):
        form = ClienteRegistroForm(request.POST)
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
        u = User.objects.get(username=user.username)
        
        cli = Cliente.objects.filter(user_cliente = u).first()
        
        rep = Repartidor.objects.filter(user = u).first()
        if(not(cli is None)):
            return redirect('cliente:HomeCliente')
        elif(not(rep is None)):
            return render(request,"repartidor/index.html")
        else:
            if(u.is_superuser):
                return render(request, "administrador/index.html")
            else:    
                return render("<h1>asdads</h1>")
@login_required                
def HomeCliente(request):
    if request.method == "GET":
        return render(request, "cliente/home.html")

class CerrarSesion(View):
    def get(self, request):
        logout(request)
        return redirect("cliente:IndexCliente")

@login_required
def CarritoView(request):
    if request.method == 'GET':

        user = request.user
        
        user_1 = User.objects.get(id=user.id)
        print(user_1)
        cliente = Cliente.objects.filter(user_cliente = user_1).first()
        print(cliente)
        carrito = Carrito.objects.filter(id_cliente_carrito = cliente.id_cliente).all()
        context = {'carrito':carrito}
        return render(request, "cliente/carrito.html", context)
'''
@login_required
def cart_add(request, pk):

    cart = Cart(request)
    product = Platillo.objects.get(id_platillo=pk)
    cart.add(product=product)
    return redirect("home")
'''
'''

@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Platillo.objects.get(id_platillo=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id_platillo=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id_platillo=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
'''
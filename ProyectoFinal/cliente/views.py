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
            user_cliente=user,
            nombre_cliente=form.cleaned_data["nombre"],
            apellido_pa_cliente=form.cleaned_data["paterno"],
            apellido_ma_cliente=form.cleaned_data["materno"],
            telefono_cliente=form.cleaned_data["telefono"],
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

        cli = Cliente.objects.filter(user_cliente=u).first()

        rep = Repartidor.objects.filter(user=u).first()
        if(not(cli is None)):
            return redirect('cliente:HomeCliente')
        elif(not(rep is None)):
            return render(request, "repartidor/index.html")
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
        cliente = Cliente.objects.filter(user_cliente=user_1).first()
        print(cliente)
        carrito = Carrito.objects.filter(
            id_cliente_carrito=cliente.id_cliente).all()

        context = {'carrito': carrito}
        return render(request, "cliente/checkout.html", context)


@login_required
def cart_add(request, pk):
    user = request.user
    user_1 = User.objects.get(id=user.id)
    cliente = Cliente.objects.filter(user_cliente=user_1).first()
    product = Platillo.objects.get(id=pk)
    agregado_carrito = Carrito(id_platillo_carrito=product.id, nombre_platillo_carrito=product.nombre,
                               id_cliente_carrito=cliente.id_cliente, precio_platillo_carrito=product.precio)
    agregado_carrito.save()
    return redirect('cliente:carrito')


@login_required
def item_clear(request, pk):
    user = request.user
    user_1 = User.objects.get(id=user.id)
    cliente = Cliente.objects.filter(user_cliente=user_1).first()
    product = Platillo.objects.get(id=pk)
    Carrito.objects.filter(id_platillo_carrito=product.id,
                           id_cliente_carrito=cliente.id_cliente).delete()
    return redirect('cliente:carrito')


@login_required
def confirmar(request):
    user = request.user
    user_1 = User.objects.get(id=user.id)
    cliente = Cliente.objects.filter(user_cliente=user_1).first()
    cliente_id = cliente.id_cliente
    # Aquí podrías obtener las direcciones del usuario para ponerlas en un form o algo así

    # Usamos get para mostrar las direcciones del usuario
    if request.method == 'GET':
        direcciones = Direccion.objects.filter(id_cliente=cliente)
        formulario = AgregarDireccion()
        contexto = {"formulario": formulario, "direcciones": direcciones}
        return render(request, "cliente/agregar_seleccionar_direccion.html", contexto)

    if request.method == 'POST':
        if 'agregar' in request.POST:
            formulario = AgregarDireccion(request.POST)
            if formulario.is_valid():
                id_cliente = cliente_id
                descripcion_direccion = formulario.cleaned_data["direccion"]
                print("******************************************************")
                print(id_cliente)
                print(descripcion_direccion)
                formulario.save()
                # return render(request, "cliente/agregar_seleccionar_direccion.html")
                return HttpResponse("Peiddo realizado")
        return HttpResponse("Error guardar direccion")

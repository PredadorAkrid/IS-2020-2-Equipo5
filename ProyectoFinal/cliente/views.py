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

from administrador.models import *
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
def ver_menu(request):
    platillos = Platillo.objects.all()
    contexto = {"platillos": platillos}
    return render(request, "cliente/ver_menu.html", contexto)


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
        contexto = {"formulario": formulario,
                    "direcciones": direcciones, "cliente": cliente}
        return render(request, "cliente/agregar_seleccionar_direccion.html", contexto)

    if request.method == 'POST':
        if 'agregar' in request.POST:
            formulario = AgregarDireccion(request.POST)
            if formulario.is_valid():
                id_cliente = formulario.cleaned_data["id_cliente"]
                descripcion_direccion = formulario.cleaned_data["descripcion_direccion"]
                formulario.save()
                return redirect('cliente:confirmar')
        if 'seleccion' in request.POST:
            # Aquí ya puedes redirigir a donde quieras con la informacion de post dejo una pagina de prueba (el post te va a mandar el id de la direccion)
            estado_orden = EstadoOrden.objects.filter(id_estado = 1).first()

            print(estado_orden)
            direccion_seleccionada = request.POST.get("seleccion", "")
            direccion_final = Direccion.objects.filter(id_direccion = direccion_seleccionada).first()
            carrito = Carrito.objects.filter(id_cliente_carrito=cliente.id_cliente).all()
            contador_precio = 0
            for elem in carrito:
                platillo_carrito_cliente = Platillo.objects.filter(id=elem.id_platillo_carrito).first()
                contador_precio += platillo_carrito_cliente.precio
            print(contador_precio)           
            orden_generada = Orden(precio_orden=contador_precio, id_cliente_orden = cliente, id_estado_orden=estado_orden, direccion_entrega_orden = direccion_final)
            orden_generada.save()
            for elem in carrito:
                platillo_carrito_cliente = Platillo.objects.filter(id=elem.id_platillo_carrito).first()
                orden_generada.id_platillo_orden.add(platillo_carrito_cliente)
            print(orden_generada)
            orden_generada.save()
            for elem in carrito:
                Carrito.objects.filter(id_platillo_carrito=elem.id_platillo_carrito, id_cliente_carrito=elem.id_cliente_carrito).delete()
            return HttpResponse("Gracias por tu compra, estamos procesando tu compra, tú número de pedido es: " + str(orden_generada.id_orden))

    return HttpResponse("Ocurrio un error interno, intentalo más tarde")


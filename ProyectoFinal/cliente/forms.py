from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpForm(UserCreationForm):
    """Sign up new user form."""
    nombre = forms.CharField(max_length=64)
    paterno = forms.CharField(max_length=100)
    materno = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=10)
    field_order = ['nombre', 'paterno','materno',  'telefono', 'email', 'password1', 'password2']
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', )


    def save(self, commit=True):
        username = self.cleaned_data.get('email')
        first_name = self.cleaned_data.get('nombre')
        last_name = self.cleaned_data.get('paterno')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password1')
        #avatar = self.clean_avatar()
        user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name,
                                        email=email, password=password)
        #user.is_active = False
        #user1 = Usuario.create_user_Usuario(user, avatar)
        #user.set_username()
        #user1 = user.get
        if commit:
            #user.save()
            #return user
            pass
        return user
    def clean_email(self):
        """Valida que el correo no exista en la base de datos"""
        data = self.cleaned_data.get('email')
        if User.objects.filter(email=data).count() > 0:
            raise forms.ValidationError("Este correo ya está registrado")
        return data
#Form para validar inicios de sesión
#Heredamos del form de autenticación de django AuthenticationForm no es
#necesario cargar los campos usaurio contraseña.
#Previamente se definió que el correo es el username
class InicioSesionForm(AuthenticationForm):
    """Login form."""
    def clean(self):

        usuario = self.data["username"]
        clave = self.data["password"]
        #Si el correo pertenece a un repartidor levantamos un error
        #Ésto es temporal puesto que iniciarán sesión de la misma forma
        #if ( (Repartidor.objects.filter(username=usuario).count() != 0)):
        #    self.add_error(
        #        "usuario", forms.ValidationError("No es un cliente")
        #    )
        #Si el correo no existe en la tabla usuarios mandamos un error de registro
        if (User.objects.filter(username=usuario).count() == 0 ):
            self.add_error(
                "username", forms.ValidationError("Éste correo no existe")
            )


        # authenticate search for the user with that username and password.
        # authenticate do not log any user.
        user = authenticate(username=usuario, password=clave)
        if user is None:
            self.add_error("password", forms.ValidationError("Contraseña inválida"))

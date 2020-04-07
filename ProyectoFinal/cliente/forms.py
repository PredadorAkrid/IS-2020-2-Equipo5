from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import * 
class SignUpForm(UserCreationForm):
    """Sign up new user form."""
    nombre = forms.CharField(max_length=64)
    paterno = forms.CharField(max_length=100)
    materno = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=10)
    field_order = ['nombre', 'paterno','materno',  'telefono', 'email', 'password', 'password2']
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', )

        
    def save(self, commit=True):
        username = self.cleaned_data.get('correo')
        first_name = self.cleaned_data.get('nombre')
        last_name = self.cleaned_data.get('paterno')
        email = self.cleaned_data.get('correo')
        password = self.cleaned_data.get('contra')
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

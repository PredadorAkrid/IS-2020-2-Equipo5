"""Users URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path
from .views import *

# Views
app_name = "usuarios"

from users import views

urlpatterns = [
    path("sign-up/", views.SignUp.as_view(), name="sign_up"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),


]
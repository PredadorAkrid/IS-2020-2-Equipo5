
from django.shortcuts import render
from django.views import View

# Create your views here.
##Function based views

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout


##Class-based-views
class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        return HttpResponseForbidden()



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
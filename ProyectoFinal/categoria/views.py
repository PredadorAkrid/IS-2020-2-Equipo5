from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Index(View):
    def get(self, request):
        return render(request, 'categoria/index.html')
    def post(self, request):
        return HttpResponseForbidden()
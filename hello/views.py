from django.shortcuts import render

# Create your views here.

# zde byc zobrazil obsa z exchsange

from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, Django World!")
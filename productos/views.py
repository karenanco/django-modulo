from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

# Create your views here.
def index(request):
     productos = Producto.objects.all()
     return render(request, 'productos/home.html',{'productos':productos} )
    


def dashboard(request):
    return HttpResponse("dashboard")


def login(request):
    return HttpResponse("login")

def register(request):
    return HttpResponse("register")

def register(request):
    return HttpResponse("register")

def venta(request):
    return HttpResponse("a vender")

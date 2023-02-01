from django.shortcuts import render, redirect
from .models import Emprendimiento
from .models import Cliente

# Create your views here.

def home(request):
    emprendimientos = Emprendimiento.objects.all()
    return render(request, "base.html",{"emprendimiento":emprendimientos})

def registrarse(request):
    return render(request, "registrarse.html")

def crear(request):
    codigo=request.POST['txtcodigo']
    correo=request.POST['txtcorreo']
    nombre=request.POST['txtnombre']
    telefono=request.POST['txttelefono']
    password=request.POST['txtpsw']

    client=Cliente.objects.create(codigo=codigo, correo=correo, nombre=nombre, telefono=telefono,password=password)
    return redirect('/')
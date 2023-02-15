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

def ingresar(request):
    return render(request, "ingresar.html")

def principal(request):
    emprendimientos = Emprendimiento.objects.all()
    return render(request, "principal.html",{"emprendimiento":emprendimientos})

def login(request):
    try:
        codigo=request.POST['username']
        client=Cliente.objects.get(codigo=codigo)
        if client.getPass()==request.POST['password']:
            emprendimientos = Emprendimiento.objects.all()
            return redirect('/principal/')
        else:
            return redirect('/noReg/')
    except:
        return redirect('/noReg/')

def informacion(request,codigo):
    emprendimiento = Emprendimiento.objects.get(codigo=codigo)
    return render(request, "informacion.html",{"emprendimiento":emprendimiento}) 

def noReg(request):
    return render(request, "noReg.html") 

def perfil(request):
    return render(request, "perfil.html")

def editar(request):
    return render(request, "editar.html")
    
def crear(request):
    return render(request, "crear.html")

def crearproducto(request):
    return render(request, "crearproducto.html")

def editarproducto(request):
    return render(request, "editarproducto.html")
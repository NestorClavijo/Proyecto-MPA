from django.shortcuts import render, redirect
from .models import Emprendimiento
from .models import Cliente
from .models import Comentario

# Create your views here.

def home(request):
    emprendimientos = Emprendimiento.objects.all()
    return render(request, "base.html",{"emprendimiento":emprendimientos})  

def registrarse(request):
    return render(request, "registrarse.html")

def crear(request):
    try:
        codigo=request.POST['txtcodigo']
        correo=request.POST['txtcorreo']
        nombre=request.POST['txtnombre']
        telefono=request.POST['txttelefono']
        password=request.POST['txtpsw']

        client=Cliente.objects.create(codigo=codigo, correo=correo, nombre=nombre, telefono=telefono,password=password)
        return redirect('/ingresar/')
    except:
        return redirect('/')

def ingresar(request):
    return render(request, "ingresar.html")

def principal(request,codigo):
    emprendimientos = Emprendimiento.objects.all()
    cliente = Cliente.objects.get(codigo=codigo)
    contexto = {"emprendimiento":emprendimientos,"cliente":cliente}
    return render(request, "principal.html",contexto)

def login(request):
    try:
        codigo=request.POST['username']
        client=Cliente.objects.get(codigo=codigo)
        if client.getPass()==request.POST['password']:
            emprendimientos = Emprendimiento.objects.all()
            return redirect('/principal/'+codigo)
        else:
            return redirect('/noReg/')
    except:
        return redirect('/noReg/')

def informacion(request,codigo):
    emprendimiento = Emprendimiento.objects.get(codigo=codigo)
    comentarios = Comentario.objects.all()
    contexto = {"emprendimiento":emprendimiento,"comentarios":comentarios}
    return render(request, "informacion.html",contexto) 

def noReg(request):
    return render(request, "noReg.html") 

def perfil(request,codigo):
    emprendimientos = Emprendimiento.objects.all()
    cliente = Cliente.objects.get(codigo=codigo)
    contexto = {"emprendimiento":emprendimientos,"cliente":cliente}
    return render(request, "perfil.html",contexto)

def editar(request):
    return render(request, "editar.html")
    
def irCrearEmprendimiento(request,codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    return render(request, "crear.html",{"cliente":cliente})

def crearEmprendimiento(request,id):
    nombre = request.POST['nombre']
    codigo = request.POST['codigo']
    descripcion = request.POST['descripcion']
    horario = request.POST['horario']
    direccion = request.POST['direccion']
    contacto = request.POST['contacto']
    cliente = Cliente.objects.get(codigo=id)
    
    emprendimiento=Emprendimiento.objects.create(codigo=codigo, descripcion=descripcion, nombre=nombre, horario=horario,direccion=direccion,contacto=contacto,cliente=cliente)
    return redirect('../perfil/'+id)

def crearproducto(request):
    return render(request, "crearproducto.html")

def editarproducto(request):
    return render(request, "editarproducto.html")

def crearComentario(request,codigo):

    cuerpo=request.POST['comentario']
    emprendimiento = Emprendimiento.objects.get(codigo=codigo)
    comentario=Comentario.objects.create( cuerpo=cuerpo,emprendimiento=emprendimiento)
    return redirect('../informacion/'+codigo)

def editarEmprendimiento(request,codigo,id):

    emprendimiento = Emprendimiento.objects.get(codigo=codigo)
    cliente = Cliente.objects.get(codigo=id)
    contexto = {"emprendimiento":emprendimiento,"cliente":cliente}
    return render(request,"editar.html",contexto)

def actualizarEmprendimiento(request,id):

    nombre = request.POST['nombre']
    codigo = request.POST['codigo']
    descripcion = request.POST['descripcion']
    horario = request.POST['horario']
    direccion = request.POST['direccion']
    contacto = request.POST['contacto']
    cliente = Cliente.objects.get(codigo=id)
    
    emprendimiento = Emprendimiento.objects.get(codigo=codigo)
    emprendimiento.nombre = nombre
    emprendimiento.descripcion = descripcion
    emprendimiento.horario = horario
    emprendimiento.direccion = direccion
    emprendimiento.contacto = contacto
    emprendimiento.cliente = cliente
    emprendimiento.save()
    return redirect('../perfil/'+id)

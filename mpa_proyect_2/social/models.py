from django.db import models

# Create your models here.

#----------------------------------//-----------------------------------//---------------

class Cliente(models.Model):
    codigo=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    telefono=models.CharField(max_length=10)
    correo=models.CharField(max_length=50)
    password=models.CharField(max_length=20)

    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.nombre, self.codigo)
    def getPass(self):
        return self.password

#----------------------------------//-----------------------------------//---------------

class Emprendimiento(models.Model):
    codigo=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    direccion=models.CharField(max_length=15)
    contacto=models.CharField(max_length=10)
    horario=models.CharField(max_length=30)
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE,null=True)

    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.nombre, self.codigo)

#----------------------------------//-----------------------------------//---------------


class Producto(models.Model):
    codigo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=20)
    decripcion=models.CharField(max_length=100)
    tipo=models.CharField(max_length=15)
    emprendimiento=models.ForeignKey(Emprendimiento, on_delete=models.CASCADE,null=True)

    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.nombre, self.tipo)

#----------------------------------//-----------------------------------//---------------

class Comentario(models.Model):
    codigo=models.AutoField(primary_key=True)
    cuerpo=models.CharField(max_length=999)
    emprendimiento=models.ForeignKey(Emprendimiento, on_delete=models.CASCADE,null=True)

    def __str__(self):
        text = "{0} ({1})"
        return text.format("comentario #", self.codigo)

#----------------------------------//-----------------------------------//---------------

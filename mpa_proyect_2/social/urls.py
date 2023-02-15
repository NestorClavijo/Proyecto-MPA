from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('register/', views.registrarse),
    path('crear/', views.crear),
    path('ingresar/', views.ingresar),
    path('login/', views.login),
    path('principal/<codigo>', views.principal),
    path('noReg/', views.noReg),
    path('informacion/<codigo>', views.informacion),
    path('perfil/<codigo>', views.perfil),
    path('editar/', views.editar),
    path('irCrearEmprendimiento/<codigo>', views.irCrearEmprendimiento),
    path('crearproducto/', views.crearproducto),
    path('editarproducto/', views.editarproducto),
    path('crearComentario/<codigo>', views.crearComentario),
    path('crearEmprendimiento/<codigo>', views.crearEmprendimiento)
]
    
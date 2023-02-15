from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('register/', views.registrarse),
    path('crear/', views.crear),
    path('ingresar/', views.ingresar),
    path('login/', views.login),
    path('principal/', views.principal),
    path('noReg/', views.noReg),
    path('informacion/<codigo>', views.informacion),
    path('perfil/', views.perfil),
    path('editar/', views.editar),
    path('crear/', views.crear),
    path('crearproducto/', views.crearproducto),
    path('editarproducto/', views.editarproducto),
]
    
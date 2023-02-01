from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('register/', views.registrarse),
    path('crear/', views.crear),
]
    
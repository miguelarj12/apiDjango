"""API9ISC22 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import Home, Inicio, Registro, Perfil, Continentes, America, LoginView, Biologia, Mexico, CuestionarioGe, Matematicas, Geografia
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='index'),
    path('inicio/', Inicio.as_view(), name='inicio'),
    path('registro/', Registro.as_view(), name='registro'),
    path('report/', views.report, name='report'),
    path('get_respuesta/', views.get_respuesta, name='get_respuesta'),
    path('perfil/', Perfil.as_view(), name='perfil'),
    path('Geografia/', Geografia.as_view(), name='Geografia'),
    path('Matematicas/', Matematicas.as_view(), name='Matematicas'),
    path('Biologia/', Biologia.as_view(), name='Biologia'),
    path('Mexico/', Mexico.as_view(), name='Mexico'),
    path('America/', America.as_view(), name='America'),
    path('Continentes/', Continentes.as_view(), name='Continentes'),
    path('CuestionarioGe/', CuestionarioGe.as_view(), name='CuestionarioGe'),
    path('login/', LoginView.as_view(), name='login'),
]


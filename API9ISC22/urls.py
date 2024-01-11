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
from django.urls import path, include
from api.views import Home, Celula, Animales, Ecosistema, Inicio, Registro, Perfil, Continentes, CuestionarioBi,  America, LoginView, Biologia, Mexico, Editar, Eliminar, CuestionarioGe, CuestionarioMa, Matematicas, Suma, Resta, Multiplicacion, Geografia
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='index'),
    path('inicio/', Inicio.as_view(), name='inicio'),
    path('registro/', Registro.as_view(), name='registro'),
    path('editar/', Editar.as_view(), name='editar'),
    path('eliminar/', Eliminar.as_view(), name='eliminar'),
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
    path('CuestionarioMa/', CuestionarioMa.as_view(), name='CuestionarioMa'),
    path('CuestionarioBi/', CuestionarioBi.as_view(), name='CuestionarioBi'),
    path('Suma/', Suma.as_view(), name='Suma'),
    path('Resta/', Resta.as_view(), name='Resta'),
    path('Multiplicacion/', Multiplicacion.as_view(), name='Multiplicacion'),
    path('Celula/', Celula.as_view(), name='Celula'),
    path('Animales/', Animales.as_view(), name='Animales'),
    path('Ecosistema/', Ecosistema.as_view(), name='Ecosistema'),
    path("", include("allauth.urls")),
]


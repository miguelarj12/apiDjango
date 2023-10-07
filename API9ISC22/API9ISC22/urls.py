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
from api.views import Home, Inicio, Registrar, acciones_Usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='index'),
    path('inicio', Inicio.as_view(), name='inicio'),
    path('registro/', Registrar.as_view(), name='registro'),
    path('crear/', acciones_Usuario.as_view(), name='acciones_Usuario'),
]

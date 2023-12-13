from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    # Agrega un related_name único para evitar conflictos
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='api_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='api_user_permissions')

# Create your models here.
class registros(models.Model): 
    nombre = models.CharField(max_length=60, null=False)
    edad = models.CharField(max_length=60, null=False)
    correo = models.CharField(max_length=100, null=False, unique=True)
    telefono = models.CharField(max_length=60, null=False)
    contrasena = models.CharField(max_length=60, null=False)

class Pregunta(models.Model):
   titulo_pregunta = models.CharField(max_length=200)

class Respuesta(models.Model):
   pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
   respuesta_pregunta = models.CharField(max_length=100)
   

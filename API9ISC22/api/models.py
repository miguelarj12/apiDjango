from django.db import models

# Create your models here.
class registros(models.Model): 
    nombre = models.CharField(max_length=60, null=False)
    edad = models.CharField(max_length=60, null=False)
    correo = models.CharField(max_length=100, null=False, unique=True)
    telefono = models.CharField(max_length=60, null=False)
    contrasena = models.CharField(max_length=60, null=False)

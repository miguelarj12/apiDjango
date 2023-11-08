from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import registros

# Create your views here.
class Home(APIView):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name)
    
class Inicio(APIView):
    template_name = 'inicio.html'
    def get(self, request):
        return render(request, self.template_name) 

class Registro(APIView):    
    def post(self, request):
        data = request.data
        new_User = registros(nombre = data.get('nombre'), edad = data.get('edad'), correo = data.get('correo'), telefono = data.get('telefono'), contrasena = data.get('contrasena'))
        try:
                subject = 'Bienvenido a tu aplicación'
                message = f'Hola {new_User.nombre}, ¡Registro exitoso!, tus datos para iniciar sesion son: Nombre: {new_User.nombre} Contraseña: {new_User.contrasena}'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [new_User.correo]
                new_User.save()
        
                send_mail(subject, message, from_email, recipient_list)
                messages.success(request, 'Correo de confirmación enviado correctamente.')          
                # return Response({'message': 'Correo de confirmación enviado correctamente'}, status=status.HTTP_201_CREATED)
                return Response({'msg': 'Usuario registrado'}, status=status.HTTP_201_CREATED)
             
        except Exception as e:
            messages.error(request, 'Error al enviar el correo de confirmación.')
            return Response({'error': 'Error al enviar el correo de confirmación'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def get(self, request):
        return render(request, 'registro.html')
            
    
    
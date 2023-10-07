from django.shortcuts import render
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

class Registrar(APIView):
    template_name = 'registro.html'
    def get(self, request):
        return render(request, self.template_name)
    
class acciones_Usuario(APIView):
    
    def post(self, request):
        data = request.data
        new_User = registros(nombre = data.get('nombre'), edad = data.get('edad'), correo = data.get('correo'), telefono = data.get('telefono'), contrasena = data.get('contrasena'))
        new_User.save()
        print(request.data)
        return Response({'msg': 'Usuario registrado'}, status=status.HTTP_201_CREATED)
    
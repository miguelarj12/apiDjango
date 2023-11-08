from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import registros
from .models import Respuesta

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
                subject = 'Bienvenido. Tu registro ha sido exitoso'
                message = f'Sea usted bienvenido {new_User.nombre}, ¡Su registro se realizo de manera correcta!, tus datos para iniciar sesion son: Nombre: {new_User.nombre} Contraseña: {new_User.contrasena}'
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

def report(request):
    if request.method == 'POST':
        dato1 = request.POST.get('grafico')

        request.session['grafico'] = dato1

        # Realiza alguna acción con los datos, como procesarlos o almacenarlos en la base de datos
        print(dato1)
    return render(request, 'report.html')


def get_respuesta(request):
    dato1 = request.session.get('grafico', None)
    if dato1:
        respuestas = Respuesta.objects.filter(pregunta=dato1)
    else:
        respuestas = Respuesta.objects.filter(pregunta=1)

    # Crear un diccionario para el conteo de respuestas
    conteo_respuestas = {}

    for respuesta in respuestas:
        pregunta_obtenida = respuesta.pregunta.titulo_pregunta
        respuesta_obtenida = respuesta.respuesta_pregunta

        # Si la respuesta ya existe en el diccionario, incrementa el conteo
        if respuesta_obtenida in conteo_respuestas:
            conteo_respuestas[respuesta_obtenida] += 1
        else:
            # Si la respuesta no existe, inicializa el conteo en 1
            conteo_respuestas[respuesta_obtenida] = 1

    # Extraer las respuestas únicas y sus conteos en listas
    respuestas_unicas_lista = list(conteo_respuestas.keys())
    conteo_valores = list(conteo_respuestas.values())
    import random
    colors = ['#'+"".join([random.choice('0123456789ABCDEF') for j in range(6)]) for _ in respuestas_unicas_lista]
    chart = {
        'title': {
            'text': pregunta_obtenida,
            'left': 'center',
        },
        'tooltip': {
            'trigger': 'item'
        },
        'toolbox': {
            'show': 1,
            'feature': {
                'mark': {'show': 1},
                'dataView': {'show': 1, 'readOnly': 0},
                'restore':{'show':1},
                'saveAsImage':{'show':1},
                }
        },
        'xAxis': [
            {
                'type': "category",
                'data':  respuestas_unicas_lista,
            }
        ],
        'yAxis': [
            {
                'type': "value",
            }
        ],
        'series': [
            {
                'data': conteo_valores,
                'type': 'bar',
            },
        ],
    }

    return JsonResponse(chart)
from api.models import Respuesta
import re

def test_descripcion_corta():
    respuesta_corta = Respuesta(respuesta_pregunta='Ayudar a personas')
    assert len(respuesta_corta.respuesta_pregunta) < 100

def test_descripcion_larga():
    respuesta_larga = Respuesta(respuesta_pregunta='Si' * 50)
    assert not len(respuesta_larga.respuesta_pregunta) > 100  

def test_descripcion_limite_exacto():
    respuesta_exacta = Respuesta(respuesta_pregunta='si' * 50)
    assert len(respuesta_exacta.respuesta_pregunta) == 100 

def test_descipcion_vacio():
    respuesta_vacio = Respuesta(respuesta_pregunta='a')
    assert not len(respuesta_vacio.respuesta_pregunta) == 0
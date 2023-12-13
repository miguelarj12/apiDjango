from api.models import Pregunta
import re

def test_descripci_corta():
    pregunta_corta = Pregunta(titulo_pregunta='Estudiante')
    assert len(pregunta_corta.titulo_pregunta) < 100

def test_descripcion_larga():
    pregunta_larga = Pregunta(titulo_pregunta='hi' * 50)
    assert not len(pregunta_larga.titulo_pregunta) > 100  

def test_descripcion_limite_exacto():
    pregunta_exacta = Pregunta(titulo_pregunta='si' * 50)
    assert len(pregunta_exacta.titulo_pregunta) == 100 

def test_descipcion_vacio():
    pregunta_vacia = Pregunta(titulo_pregunta='a')
    assert not len(pregunta_vacia.titulo_pregunta) == 0


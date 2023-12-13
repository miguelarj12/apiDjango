from api.models import registros
import re

def test_usuario_corta():
    celular_corto = registros(telefono='5587631479')
    assert len(celular_corto.telefono) < 11

def test_usuario_larga():
    correo_largo = registros(correo='miguelarj12@gmail.com')
    assert not len(correo_largo.correo) > 21 

def test_usuario_limite_exacto():
    edad_exacta = registros(edad='12')
    assert len(edad_exacta.edad) == 2

def test_usuario_vacio():
    nombre_vacio = registros(nombre='Miguel')
    assert not len(nombre_vacio.nombre) == 0
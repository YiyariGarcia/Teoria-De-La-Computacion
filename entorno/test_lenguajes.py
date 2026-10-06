import pytest
from lenguajes import (
    obtener_prefijos, obtener_sufijos, obtener_subcadenas, 
    calcular_cerradura, estimar_cantidad_cadenas
)

def test_cadena_vacia():
    assert obtener_prefijos("") == [""]
    assert obtener_sufijos("") == [""]
    assert obtener_subcadenas("") == [""]

def test_longitud_uno():
    assert obtener_prefijos("a") == ["", "a"]
    assert obtener_sufijos("a") == ["", "a"]

def test_alfabeto_un_simbolo():
    # Para n=2 con alfabeto "a", Σ* debe ser ["", "a", "aa"]
    assert calcular_cerradura("a", 2, es_positiva=False) == ["", "a", "aa"]
    # Para n=2 con alfabeto "a", Σ+ debe ser ["a", "aa"]
    assert calcular_cerradura("a", 2, es_positiva=True) == ["a", "aa"]

def test_diferencia_cerraduras_longitud_cero():
    # Para longitud 0, Σ* incluye la cadena vacía, Σ+ es conjunto vacío
    assert calcular_cerradura("a", 0, es_positiva=False) == [""]
    assert calcular_cerradura("a", 0, es_positiva=True) == []

def test_limite_cadenas():
    # Alfabeto de 10 símbolos, longitud 6 genera 1,111,111 cadenas > 200,000
    with pytest.raises(ValueError):
        calcular_cerradura("abcdefghij", 6)
import pytest
from escola.calcularMedia import calcular_media

def test_calcular_media_lista_vazia():
    # Definindo entrada
    entrada = []

    # Executando uma função e esperando o erro
    with pytest.raises(ValueError, match = "it is not allowed to send an empty list"):
        calcular_media(entrada)


def test_calcular_media_com_string():

    entrada = "hi"

    with pytest.raises(TypeError, match = "invalid note: texts are not allowed"):
        calcular_media(entrada)


def test_calcular_media_com_numero_menor_que_0():

    entrada = [1.0, -10.0]

    with pytest.raises(ValueError, match = "grades can be from 0 to 10"):
        calcular_media(entrada)


def test_calcular_media_com_numero_maior_que_10():

    entrada = [1.0, 11.0]

    with pytest.raises(ValueError, match = "grades can be from 0 to 10"):
        calcular_media(entrada)
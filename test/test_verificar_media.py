from escola.VerificaMedia import verificar_media
import pytest

def test_verificar_media_com_string():

    entrada = "ola"

    with pytest.raises(TypeError, match = "É necessário que seja um número"):
        verificar_media(entrada)


def test_verificar_media_numero_menor_que_0():

    entrada = -1

    with pytest.raises(ValueError, match = "Nota deve estar entre 0 e 10"):
        verificar_media(entrada)

def test_verificar_media_numero_maior_que_10():

    entrada = 11
    
    with pytest.raises(ValueError, match = "Nota deve estar entre 0 e 10"):
        verificar_media(entrada)
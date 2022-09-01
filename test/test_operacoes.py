import pytest
from matematica.Calculadora import soma, sub, multiplicacao, divisao, media_lista_valores

@pytest.mark.op_simples
@pytest.mark.positivos
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 12 == soma(v1, v2)

def test_soma_valor_positivo_e_negativo():
    v1 = - 5.0
    v2 = 7.0
    assert 2 == soma(v1, v2)

def test_soma_valor_negativo_e_negativo():
    v1 = - 5.0
    v2 = - 7.0
    assert -12 == soma(v1, v2)

def test_sobtracao_de_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert -2 == sub(v1, v2)

@pytest.mark.positivos
def test_multiplicacao_de_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 35 == multiplicacao(v1, v2)

@pytest.mark.positivos
def test_divisao_de_dois_valores_positivos():
    v1 = 6.0
    v2 = 2.0
    assert 3.0 == divisao(v1, v2)

@pytest.mark.positivos
def test_lista_da_media_de_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 6.0 == media_lista_valores([v1, v2])

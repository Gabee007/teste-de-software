from calculadora import soma, subtracao, multiplicacao, divisao
import pytest

def test_soma():
    assert soma(1, 3) == 4.0

def test_subtracao():
    assert subtracao(5, 3) == 2.0

def test_multiplicacao():
    assert multiplicacao(4, 3) == 12.0

def test_divisao():
    assert divisao(10, 2) == 5.0

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)

    
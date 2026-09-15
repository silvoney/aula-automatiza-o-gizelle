from app.calculadora import (
    somar,
    subtrair,
    calcular_descont,
    multiplicar
)


def test_somar():
    resultado = somar(2, 3)
    assert resultado == 5


def test_subtrair():
    resultado = subtrair(10, 4)
    assert resultado == 6


def test_calcular_desconto():
    resultado = calcular_descont(100, 10)
    assert resultado == 90


def test_multiplicar():
    resultado = multiplicar(4, 5)
    assert resultado == 20

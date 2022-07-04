'''
Tomando como base el ejercicio anterior, crear una función test_calcula_raiz() donde se deberán crear 
varios casos de prueba para asegurar que los resultados de la función calcula_raiz sean correctos
'''
from scipy.optimize import bisect
import matplotlib.pylab as plt
import numpy as np


def calcula_raiz(a, b, c):
    assert type(a) == int and type(b) == int and type(c) == int
    assert a != 0 and b != 0

    f = lambda x: a*x**2 + b*x + c

    x1 = bisect(f, -10, 0, xtol=1e-6)
    x2 = bisect(f, 0, 10, xtol=1e-6)

    return x1, x2


def test_calcula_raiz():
    #Valores de prueba que no producen un error en la función
    assert calcula_raiz(1, 5,-2)
    assert calcula_raiz(-2, 5, 4)
    assert calcula_raiz(2, -3, -4)
    assert calcula_raiz(-2, -5, 4)
    assert calcula_raiz(1, -9, 0)

    #Valores de prueba que producen un error en la función
    assert calcula_raiz(9, 0,10)
    assert calcula_raiz(0, -10, 25)


def main():
    test_calcula_raiz()


if __name__ == '__main__':
    main()
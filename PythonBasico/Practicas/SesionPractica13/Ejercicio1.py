'''
Se requiere construir un programa que encuentre las raíces de una función del tipo ax2 + bx + c = 0.
Los valores de los coeficientes: a, b, c serán estáticos y puestos manualmente en el código. Para este 
ejercicio, crear una función calcula_raiz(a, b, c) y colocar los assert necesarios al inicio de la 
función para validar las entradas.
Nota: se debe validar que las entradas sean numéricas
''' 
from scipy.optimize import bisect
import matplotlib.pylab as plt
import numpy as np


def calcula_raiz(a, b, c):
    '''Calcula las raices de una funcion cuadráica cuyos coeficientes y termino independiente bienen dados por el usuario.
    PARAMS
    ------
    a : int
        coeficiente numérico de x^2.
    b : int
        coeficiente numérico de x.
    c : int 
        Término independiente.
    RETURN
    ------
    x1 : float
        raíz en el intervalo -10 y 0.
    x2 : float
        raíz en el intervalo 0 y 10.
    '''
    # Evaluamos que los parametros sean de tipo entero.
    assert type(a) == int and type(b) == int and type(c) == int
    # Evaluamos que los coeficientes sean diferentes de cero.
    assert a != 0 and b != 0

    # Funcion cuadrática
    f = lambda x: a*x**2 + b*x + c

    # Generamos un array con 20 números entre -10 y 10, graficamos la función en ese intervalo.
    ind = np.linspace(-10, 10, 20)
    fig, ax = plt.subplots(1, 1, figsize=(15, 5))
    ax.plot(ind, list(map(f, np.linspace(-10, 10, 20))))
    plt.show()

    # Calcula las raices de la función en los intervalos (-10,0), (0,10)
    x1 = bisect(f, -10, 0, xtol=1e-6)
    x2 = bisect(f, 0, 10, xtol=1e-6)

    return x1, x2


def main():
    raiz1, raiz2 = calcula_raiz(2, 5, -9)
    print(f'\nRaíz N°1: {raiz1}, Raíz N°2: {raiz2}\n')


if __name__ == '__main__':
    main()
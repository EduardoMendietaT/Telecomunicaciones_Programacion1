'''
El volumen de una concha esférica es la diferencia entre el volumen de la esfera exterior y la esfera inferior. 
Su fórmula es la siguiente: 4/3pi(R^3 - r^3).

Crear una función que tome como parámetros dos arrays de numpy de tipo flotante (R y r), donde Ri y ri son los valores 
de radio exterior e inferior para la esfera i. La función retornará un array de numpy con los valores de volumen calculados 
para todas las esferas i.

Para este ejercicio deberá crear valores de prueba para R y r de forma aleatoria. La función que calcula el volumen deberá 
probar que los tipos de datos de entrada, i.e. R y r, sean los correctos. También que ambos arrays tengan el mismo número 
de elementos. Adicionalmente, que Ri > ri.

Cree una función para probar que su implementación funcione correctamente. Valores de prueba:
- con R=3 y r=3, salida: 0
- con R=7 y r=2, salida: ~1403.2447
'''

import numpy as np
import math
import random

# Calcula el volumen de la concha esferica de una esfera.
volumen_concha_esferica = lambda R, r: 4/3 * math.pi * (math.pow(R, 3) - math.pow(r, 3))


def calcular_volumenes(R, r):
    '''Calcula el volumen de las conchas esfericas usando los radios pasados como parametros.
    PARAMS
    ------
    R : numpy.ndarray
        valores de radios exteriores de las esferas.
    r : numpy.ndarray
        valores de radios inferiores de las esferas.
    RETURN
    ------
    volumenes : numpy.ndarray
        lista con los volumenes calculados.
    '''
    assert type(R) == np.ndarray and type(r) == np.ndarray
    assert len(R) == len(r)
    size = len(R)
    volumenes = np.zeros(size)
    for i in range(size):
        assert type(R[i]) == np.float64 and type(r[i]) == np.float64
        assert R[i] >= r[i]
        volumenes[i] = round(volumen_concha_esferica(R[i], r[i]), 4)
    return volumenes


def test_calcular_volumenes():
    '''Casos de prueba solicitados por el docente.
    '''
    volumenes = calcular_volumenes(np.array([3.0, 7.0]), np.array([3.0, 2.0]))
    assert volumenes[0] == 0.0
    assert volumenes[1] == 1403.2447

    print(f'\nValores de prueba: {volumenes}\n')


def main():
    test_calcular_volumenes()

    # Arrays con valores randoms de radios exteriores e interiores de un número 'size' de esferas.
    size = random.randint(2, 20)
    R = np.random.normal(10, 3, size)
    r = np.random.normal(10, 3, size)
    calcular_volumenes(R, r)


if __name__ == '__main__':
    main()
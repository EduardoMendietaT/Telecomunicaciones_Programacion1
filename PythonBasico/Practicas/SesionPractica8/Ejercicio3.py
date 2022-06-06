'''
Cuando se aplica una operación matemática a un array de numpy, se aplica la misma operación elemento 
por elemento y como resultado se obtiene un nuevo array. Ejemplo:

x = np.arange(10)
print(x**2)

[ 0  1  4  9 16 25 36 49 64 81]

Teniendo esto en cuenta, se requiere crear un programa que calcule los valores de la siguiente función:
f(x) = x^2 - 3x - 10 para -10 <= x <= 20

Genere 50 valores en este rango (puede hacer uso de la función linspace de numpy) y calcule los valores 
de la función. La idea de este ejercicio no es recorrer elementos individualmente, sino aplicar una 
función a todos los elementos. Finalmente, ejecutar la función mostrar(x, y) para mostrar en pantalla 
los valores de la función.
'''
import matplotlib.pylab as plt
%matplotlib inline  


def mostrar(x, y):
    """
    muestra en pantalla los valores de `x` y `y`
    
    :param x: np.array, array con los valores en x 
    :param y: np.array, array con los valores en y
    
    """
    plt.plot(x, y)
    plt.show()
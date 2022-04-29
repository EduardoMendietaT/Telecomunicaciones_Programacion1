'''
Importe la librería math mediante el siguiente comando import math. Luego, genere un array estático
con valores punto flotante de 10 elementos. Se requiere calcular el valor promedio de este array, pero
únicamente tomando en cuenta el valor absoluto de los distintos elementos. Luego el programa deberá calcular
el factorial de la parte entera del resultado anterior.
'''
import math

# Array estático con valores punto flotante.
x = [33.5, 4.4, -5.5, 2.2, -7.7, 9.9, 11.2, 33.2, 66.5, -33.1]

# Generamos una lista con los valores absolutos de los elementos de 'x'.
valores_absolutos = [abs(i) for i in x]

# calculamos el promedio de los elementos de 'valores_absolutos'.
suma = 0
for i in valores_absolutos:
    suma += i
promedio = suma/len(valores_absolutos)
print(f'\n{valores_absolutos}\nEl promedio es: {round(promedio, 2)}')

# Calculamos el factorial de la parte entera del promedio anterior.
factorial = 1
for i in range(1, int(promedio + 1)):
    factorial *= i
print(f'\nEl factorial de {int(promedio)} es: {factorial}.\n')

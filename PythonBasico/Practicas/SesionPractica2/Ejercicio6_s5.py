'''
Escribir un programa para construir el siguiente patron:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
import random

# Generamos un número de lineas aleatorio.
num_lineas = random.randint(1, 20)
print(f'\nNúmero de líneas = {num_lineas}:\n')

# creamos un string con una cantidad de '*' igual al número de lineas.
linea = '* ' * num_lineas

# Imprimimos '* ' en orden creciente hasta la(s) linea(s) central(es) y luego en sentido decreciente.
for i in range(1, num_lineas + 1):
    if round(num_lineas / 2) >= i:
        print(linea[: i * 2 ])
    else:
        print(linea[i * 2 - 2:])
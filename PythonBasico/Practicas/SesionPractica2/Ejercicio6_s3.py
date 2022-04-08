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
num_lineas = random.randint(1, 15)
print(f'\nNúmero de líneas: {num_lineas}\n')

# Establecemos el límite central.
limite = int(num_lineas / 2)
if num_lineas % 2 != 0:
    limite = limite + 1

# creamos un string con una cantidad de '*' igual al número de lineas.
linea = ''
for i in range(num_lineas):
    linea += '*'

# Imprimimos '*' en orden creciente hasta la(s) linea(s) central(es) y luego en sentido decreciente.
for i in range(1, num_lineas + 1):
    if i <= limite:
        print(linea[:i])
    else:
        print(linea[i - 1:])

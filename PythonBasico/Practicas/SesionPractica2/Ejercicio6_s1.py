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

caracter = '*'

# Generamos un número de lineas aleatorio.
num_lineas = random.randint(1, 30)
print(f'\nNúmero de lineas = {num_lineas}:\n')

# Creamos una cadena con una cantidad de caracteres igual al número de lineas.
cadena = caracter * num_lineas

# Establecemos el límite central.
if num_lineas % 2 == 0:
    linea_central = num_lineas / 2
else:
    linea_central = int(num_lineas / 2) + 1

# Imprimimos '*' en orden creciente hasta la(s) linea(s) central(es) y luego en sentido decreciente.
for i in range(1, num_lineas + 1):
    if linea_central >= i:
        print(caracter * i)
    else:
        print(cadena[:num_lineas - (i - 1)]) 
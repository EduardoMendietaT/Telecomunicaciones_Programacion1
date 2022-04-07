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

# Validamos cuantos caracteres lleva la linea central en base a si la cantidad 
# de lineas es par o impar.
if num_lineas % 2 == 0:
    linea_central = num_lineas / 2
else:
    linea_central = int(num_lineas / 2) + 1

# Imprimimos la cantidad de caracteres dependiendo de la linea central. 
for i in range(1, num_lineas + 1):
    if linea_central >= i:
        print(caracter * i)
    else:
        # restamos 1 a 'i' revertir hacia abajo la cantidad de caracteres desde la linea central.
        print(cadena[:num_lineas - (i - 1)]) 
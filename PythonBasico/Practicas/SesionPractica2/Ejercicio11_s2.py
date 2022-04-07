'''
Escribir un programa para construir el siguiente patrón:
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''
import random

# Generamos un número de lineas aleatorio.
num_lineas = random.randint(1, 100)
print(f'\nNúmero de lineas = {num_lineas}:\n')

# Convertimos a 'i' en una cadena y extraemos su ultimo elemento.
# Imprimimos el caracter tantas veces como la variable 'i'.
for i in range(1, num_lineas + 1):
    cadena = f'{i}'[-1] * i
    print(cadena)

print('\n')
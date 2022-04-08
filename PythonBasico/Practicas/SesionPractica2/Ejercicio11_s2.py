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

# Imprimimos la cadena el número de veces de la variable 'num_lineas'.
for i in range(1, num_lineas + 1):
    cadena = ''
    # Generamos la cadena concatenando la variable 'i' tantas veces como su valor.
    for j in range(i):
        cadena += f'{i}'[-1] # Obtenemos el último elemento de la cadena para concatenar.
    print(cadena)

print('\n')
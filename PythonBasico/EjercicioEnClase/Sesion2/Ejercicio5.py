'''
Ejercicio ciclo for: Se requiere conocer la multiplicación de los n primeros 
números enteros > 0
'''
import random

n = random.randint(2, 10)
resultado = 1
operacion = ''

for i in range(1, n+1):
    if i < n:
        operacion += f'{i} x '
    else:
        operacion += f'{i}'
    resultado *= i

print(f'La multiplicación de {operacion} es: {resultado}')
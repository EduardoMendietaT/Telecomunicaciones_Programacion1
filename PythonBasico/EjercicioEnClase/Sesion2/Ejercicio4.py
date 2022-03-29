'''
Dados 3 números (a, b, c) encuentre el número mayor
'''
import random

# a, b y c son números enteros random entre 1 y 20.
a = random.randint(1, 20)
b = random.randint(1, 20)
c = random.randint(1, 20)

print(f' a = {a}, b = {b}, c = {c}.')

# comprobamos ¿Cuál de los 3 números es mayor?
if a > b:
    num_mayor = a if a > c else c
elif b > c:
    num_mayor = b
else:
    num_mayor = c

print(f'El número mayor es: {num_mayor}.')

# Solución Profe:
if a > b and a > c:
    num_mayor = a
elif b > c:
    num_mayor = b
else:
    num_mayor = c

print(f'El número mayor es: {num_mayor}.')
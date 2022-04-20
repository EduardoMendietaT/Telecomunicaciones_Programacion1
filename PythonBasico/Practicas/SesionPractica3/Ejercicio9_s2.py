'''
Escriba un programa que calcule la descomposición en factores primos de un número.
Ejemplo para 500: Salida: 2 2 5 5 5
'''
numero = int(input('\nIngrese un número para descomponerlo en sus factores primos: '))

# Creamos una lista vacía para almacenar todos los factores primos del número.
factores_primos = []

# Iniciamos con el primer número primo.
factor = 2

while numero != 1:

    # Validamos que el 'num_primo' pertenesca a los factores primos del número y lo almacenamos.
    while numero % factor == 0:
        numero = numero // factor
        factores_primos += [factor]

    # Continuamos con el siguiente número primo.
    factor += 1

print(f'\nFactores primos: {factores_primos}')

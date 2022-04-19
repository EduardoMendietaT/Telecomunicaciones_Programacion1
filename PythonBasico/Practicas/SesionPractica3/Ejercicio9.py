'''
Escriba un programa que calcule la descomposición en factores primos de un número.
Ejemplo para 500: Salida: 2 2 5 5 5
'''
numero = int(input('\nIngrese un número para descomponerlo en sus factores primos: '))

# Creamos una lista vacía para almacenar todos los factores primos del número.
factores_primos = []

# Iniciamos con el primer número primo.
num_primo = 2

while numero != 1:

    es_primo = True

    # Validamos que el valor de 'num_primo' sea un número primo.
    i = 2
    while es_primo and i < num_primo:
        if num_primo % i == 0:
            es_primo = False
        i += 1

    if es_primo:
        # Validamos que el 'num_primo' pertenesca a los factores primos del número y lo almacenamos.
        while numero % num_primo == 0:
            numero = numero // num_primo
            factores_primos += [num_primo]

    # Continuamos con el siguiente número primo.
    num_primo += 1

print(f'\nFactores primos: {factores_primos}')

'''
Generar una lista con números de 20 a 40, con incrementos de 5 y calcule su suma usando un ´for´.
'''
# Generamos una lista con números desde el 20 al 40, incrementando de 5 en 5.
start, stop, step = 20, 40, 5
numeros = list(range(start, stop + 1, step))

# Sumamos todos los números de la lista.
suma = 0
for numero in numeros:
    print(numero)
    suma += numero

print(f'La suma es: {suma}.\n')
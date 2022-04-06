'''
'''
# Solución 1: --------------------------------------------------------------------
# Generamos una lista que inicia en 20, termina en 40 y con un incremento de 5.
inicio, limite, incremento = 20, 40, 5
numeros = list(range(inicio, limite + 1, incremento))

suma = 0
# Generamos una cadena indicando los numeros que se suman.
cont = 1
numeros_str = ''

# Calculamos la suma de los números de la lista
for i in numeros:
    numeros_str += f'{i}+' if cont < len(numeros) else f'{i}'
    suma += i
    cont += 1

print(f'\n{numeros_str} = {suma}\n')

# Solución 2: --------------------------------------------------------------------
suma = 0

# Calculamos la suma de una lista de numeros.
for i in range(20, 41, 5):
    print(i)
    suma += i

print(f'La suma es: {suma}.\n')
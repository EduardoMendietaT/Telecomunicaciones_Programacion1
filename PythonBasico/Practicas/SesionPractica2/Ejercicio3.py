'''
1. Modifique el código del Ejercicio 1, para que en vez de mostrar la suma total de los elementos, 
muestre la multiplicación de los mismos.

2. Ahora modifique su código de forma tal que se muestre la multiplicación de los
primeros 10 números mayores a 0.
'''
# 1. Multiplicacion de los números 0-9
multiplicacion = 1
for i in range(10):
    multiplicacion *= i
    print(i)

print(f'La multiplicación es: {multiplicacion}.\n')

# 2. Multiplicación de los 10 primeros números mayores a cero
start, stop = 1, 10
multiplicacion = 1

for i in range(start, stop + 1):
    print(i)
    multiplicacion *= i

print(f'La multiplicación es: {multiplicacion}.\n')
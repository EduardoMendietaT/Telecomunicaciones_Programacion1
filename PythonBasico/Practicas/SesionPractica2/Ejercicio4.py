'''
1. Implemente un código que muestre los números enteros x tal que 0 < x <= 30 y x sea par
2. Modifique su código para que muestre la suma de los numeros impares en el mismo rango
'''

# 1. Generamos e imprimimos los números pares en el rango 0 < x <= 30
start, stop, step = 0, 30, 2

for i in range(start, stop + 1, step):
    print(i)

print('\n')

# 2. Suma de los números impares en el rango 0 < x <= 30
start, stop, step = 1, 30, 2
suma = 0

for i in range(start, stop + 1, step):
    print(i)
    suma += i

print(f'La suma es: {suma}.\n')
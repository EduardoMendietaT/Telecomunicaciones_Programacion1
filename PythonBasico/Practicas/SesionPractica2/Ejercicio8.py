'''
En este ejercicio se pretende que el estudiante use for aninados.
Se tienen 2 conjuntos de numeros enteros x = [1,2,...,10] e y = [11,12,...,15]. Escribir un programa que muestre en
pantalla todas las posibles combinaciones xi, yi
'''
# Construimos los conjuntos x = [1,2,...,10] e y = [11,12,...,15].
x = list(range(1, 11))
y = list(range(11, 16))

print('\nPosibles combinaciones (xi, yj):')

#Imprimimos las posibles combinaciones (xi, yj).
for xi in x:
    print('\n----\n')
    for yj in y:
        print(f'({xi},{yj})')

print('\n')
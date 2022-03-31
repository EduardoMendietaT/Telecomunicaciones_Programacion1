'''
Se requiere comparar un número ingresado, x, con otros números previamente almacenados para determinar:
- Cuantos números iguales a x existen.
- Cuantos números mayores a x existen.
- Cuantos números menores a x existen.
'''

x = int(input("\nIngrese el valor de x: "))

# números previamente almacenados
num1 = 10
num2 = 5
num3 = 4
num4 = 6
num5 = 3

# Solución 1: ****************************************************
cont_iguales = 0
cont_mayores = 0
cont_menores = 0

if x == num1 or x == num2 or x == num3 or x == num4 or x == num5:
    cont_iguales += 1
if x > num5:
    cont_menores += 1
    if x > num3:
        cont_menores += 1
        if x > num2:
            cont_menores += 1
            if x > num4:
                cont_menores += 1
                if x > num1:
                    cont_menores += 1
if x < num1:
    cont_mayores += 1
    if x < num4:
        cont_mayores += 1
        if x < num2:
            cont_mayores += 1
            if x < num3:
                cont_mayores += 1
                if x < num5:
                    cont_mayores += 1
print(f'\nExisten {cont_iguales} número(s) igual(es) a {x}, {cont_mayores} número(s) mayor(es)\
 a {x} y {cont_menores} numero(s) menor(es) a {x}.\n')

# Solución 2: ****************************************************
cont_iguales = 0
cont_mayores = 0
cont_menores = 0

numeros = {num1, num2, num3, num4, num5} # Creamos un conjunto: no posee elementos repetidos.

if x in numeros:
    cont_iguales = 1

numeros.add(x)
numeros = sorted(numeros) # Ordenamos el conjunto.

if 0 < numeros.index(x) < len(numeros) - 1: # evaluamos si la posición de x esta en el rango [1, n-1].
    cont_menores = numeros.index(x) # al no tomar en cuenta la posicion 0 el indice se vuelve la cantidad de numeros menores.
    cont_mayores = len(numeros) - (numeros.index(x) + 1)
elif x == numeros[-1]: # -1 devuelve el ultimo elemento de la lista
    cont_menores = len(numeros) - 1 
else:
    cont_mayores = len(numeros) - 1

print(f'\nExisten {cont_iguales} número(s) igual(es) a {x}, {cont_mayores} número(s) mayor(es)\
 a {x} y {cont_menores} numero(s) menor(es) a {x}.\n')
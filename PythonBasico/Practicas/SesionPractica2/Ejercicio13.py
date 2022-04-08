'''
La solución del ejercicio 7 de la sesión de ejercicios 2 puede ser mejorada con el uso de un for.
Implemente el código necesario. A continuación el enunciado del ejercicio:
Se requiere comparar un número ingresado, , con otros números previamente almacenados para determinar:
    - Cuantos números iguales a x existen.
    - Cuantos números mayores a x existen.
    - Cuantos números menores a x existen.
'''
x = int(input('\nIngrese el valor de x: '))

# números previamente almacenados
numeros = [10, 5, 4, 6, 3]

#son variables contadores
mayores = 0
menores = 0
iguales = 0

#se compara si el valor de 'i' es mayor, menor o igual a 'x'.
for i in numeros:
    if x > i:
        menores += 1
    elif x < i:
        mayores += 1
    else:
        iguales += 1

print(f'\nExisten {mayores} números mayor(es), {menores} menor(es) y {iguales} igual(es) a {x}.\n')
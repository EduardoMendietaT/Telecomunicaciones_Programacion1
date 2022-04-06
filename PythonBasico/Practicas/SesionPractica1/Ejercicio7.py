'''
Se requiere comparar un número ingresado, x, con otros números previamente almacenados para determinar:
    - Cuantos números iguales a  existen.
    - Cuantos números mayores a  existen
    - Cuantos números menores a  existen
'''
x = int(input('\nIngrese el valor de x: '))

# números previamente almacenados
num1 = 10
num2 = 5
num3 = 4
num4 = 6
num5 = 3

#son variables contadores
mayores = 0
menores = 0
iguales = 0

#se compara si el valor es mayor, menor o igual al número 1.
if x > num1:
    menores += 1
elif x < num1:
    mayores += 1
else:
    iguales += 1
#se compara si el valor es mayor, menor o igual al número 2.
if x > num2:
    menores += 1
elif x < num2:
    mayores += 1
else:
    iguales += 1
#se compara si el valor es mayor, menor o igual al número 3.
if x > num3:
    menores += 1
elif x < num3:
    mayores += 1
else:
    iguales += 1
#se compara si el valor es mayor, menor o igual al número 4.
if x > num4:
    menores += 1
elif x < num4:
    mayores += 1
else:
    iguales += 1
#se compara si el valor es mayor, menor o igual al número 5.
if x > num5:
    menores += 1
elif x < num5:
    mayores += 1
else: 
    iguales += 1

print(f'\nExisten {mayores} números mayor(es), {menores} menor(es) y {iguales} igual(es) a {x}.\n')
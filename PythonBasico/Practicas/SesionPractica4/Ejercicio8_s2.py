'''
Leer del usuario un número entero positivo, e indique cuantas unidades, decenas, centenas, y miles posee.
Por ejemplo: 4567
7 unidades, 6 decenas, 5 centenas, 4 miles.
Considere que cuando sea una unidad, 1 decena, etc. la palabra es en singular
'''
numero = int(input('\nIngrese un número entero positivo: '))

cont_decenas = 0
cont_centenas = 0
cont_miles = 0

mensaje = f'El número {numero} tiene: '
while numero >= 10:
    if numero - 1000 >= 0:
        numero -= 1000
        cont_miles += 1
    elif numero - 100 >= 0:
        numero -= 100
        cont_centenas += 1
    elif numero - 10 >= 0:
        numero -= 10
        cont_decenas += 1

if numero != 1:
    mensaje += f', {numero} unidades'
else:
    mensaje += f', {numero} unidad'

if cont_decenas != 1:
    mensaje += f', {cont_decenas} decenas'
else:
    mensaje += f', {cont_decenas} decena'

if cont_centenas != 1:
    mensaje += f', {cont_centenas} centenas'
else:
    mensaje += f', {cont_centenas} centena'

if cont_miles != 1:
    mensaje += f', {cont_miles} miles'
else:
    mensaje += f', {cont_miles} mil'

print(f'\n{mensaje}.\n')

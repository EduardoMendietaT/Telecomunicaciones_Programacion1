'''
Leer del usuario un número entero positivo, e indique cuantas unidades, decenas, centenas, y miles posee.
Por ejemplo: 4567
7 unidades, 6 decenas, 5 centenas, 4 miles.
Considere que cuando sea una unidad, 1 decena, etc. la palabra es en singular
'''
numero_str = input('\nIngrese un número entero positivo: ')

# Validamos que la entrada sea un número entero.
if not numero_str.isdigit() or int(numero_str) < 1:
    print(f'\nLa entrada: "{numero_str}", no es un número entero positivo!\nEl programa ha finalizado!\n')
    exit()

# Extraemos en una lista todas las cifras que componen al número:
cifras = [int(i) for i in numero_str]

# Recorremos todas las cifras del número iniciando por las unidades,
# verificamos cuantas unidades, decenas, centenas y miles hay.
mensaje = f'El número {numero_str} tiene: '
for i in range(1, len(cifras) + 1):
    if i == 1:
        mensaje += f'{cifras[-i]} unidades' if cifras[-i] != 1 else f'1 unidad'
    if i == 2:
        mensaje += f', {cifras[-i]} decenas' if cifras[-i] != 1 else f', 1 decena'
    if i == 3:
        mensaje += f', {cifras[-i]} centenas' if cifras[-i] != 1 else f', 1 centena'
    if i == 4:
        aux = [f'{j}' for j in cifras[:len(cifras) - 3]]
        num = int(''.join(aux))
        mensaje += f', {num} miles' if num != 1 else f', 1 mil'

print(f'\n{mensaje}.\n')

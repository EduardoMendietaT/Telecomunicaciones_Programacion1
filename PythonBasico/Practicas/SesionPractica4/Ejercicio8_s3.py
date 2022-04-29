'''
Leer del usuario un número entero positivo, e indique cuantas unidades, decenas, centenas, y miles posee.
Por ejemplo: 4567
7 unidades, 6 decenas, 5 centenas, 4 miles.
Considere que cuando sea una unidad, 1 decena, etc. la palabra es en singular
'''
# Pedimos un número entero positivo y creamos una lista de categorias.
numero_str = input('\nIngrese un número entero positivo: ')
categorias = [['unidades', 0], ['decenas ', 0], ['centenas ', 0], ['miles', 0]]

# Validamos que la entrada sea un número entero.
if not numero_str.isdigit() or int(numero_str) < 1:
    print(f'\nLa entrada: "{numero_str}", no es un número entero positivo!\nEl programa ha finalizado!\n')
    exit()

numero = int(numero_str) # Transformamos a entero la entrada del usuario.
posicion_categoria = len(categorias) - 1 # Iniciamos la poicion desde la poicion mayor.
sustraendo = 1000 # Valor base establecido en el ejercicio.
while numero >= 10:
    if numero - sustraendo >= 0: # Evalumas cuantas veces esta el 1000, 100 y 10 en el número
        numero -= sustraendo
        total = categorias[posicion_categoria][1]
        categorias[posicion_categoria][1] = total + 1
    else: # Actualizamos la base y el contador de categoria.
        sustraendo //= 10
        posicion_categoria -= 1
categorias[0][1] = numero # El número restante son las unidades existentes.

# Imprimos la cantidad de veces que aparece una categoria coniderando palabras en singular/plural.
mensaje = f'El número {numero_str} tiene'
i = 0
while i < len(categorias):
    cat = categorias[i]
    mensaje += f', {cat[1]} {cat[0].strip()}' if cat[1] != 1 else f', 1 {cat[0][:len(cat[0])-2]}'
    i += 1

print(f'\n{mensaje}.\n')

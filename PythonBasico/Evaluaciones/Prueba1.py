'''
Considerando una lista de tamaño variable, cuyos elementos son de tipo string de 6 caracteres de longitud
donde los primeros 4 caracteres son texto aleatorio y los últimos 2 caracteres son números que van del 1 al
99, se requiere un programa que considerado únicamente los números de la lista, los categorice de la siguiente
manera: inicialmente se le pedirá al usuario que ingrese cuantas categorías necesita. Posteriormente, en función
de este número, se procederá a analizar individualmente los números obtenidos de la lista inicial y colocarlos en
las distintas categorías.

Por ejemplo, si se tiene la siguiente lista de palabras:
 - lista = ['bddd64', 'bdbc67', 'baaa36', 'bacd24', 'cbda41', 'bbab33']
 - y el usuario pide 2 categorías, el resultado deberá ser que existen 4 números (36, 24, 41, 33)
   en la primera categoría y 2 números (64, 67) en la segunda.
'''
# Lista con cadenas previamente almacenadas.
lista = ['dbdd47', 'dcaa37', 'dadd78', 'dbba37', 'acbb52', 'adad45', 'addd43', 'bbdb82', 'aaab22', 'bbac84', 'bcca83', 'adbc16', 'aabd48', 'abdb59', 'dbba51',
         'dbad46', 'cbca12', 'dccc66', 'dcba81', 'bbbc21', 'bbda25', 'abdb55', 'bbda36', 'aaad29', 'bdda17', 'aaab35', 'cacd19', 'adcc39', 'adbb87', 'bddc49',
         'abdd92', 'bdab35', 'acab81', 'babc89', 'bbba58', 'bcdc58', 'bcad98', 'dbdd52', 'cdac22', 'bbad38', 'adbc53', 'dcab49', 'ccad14', 'cbac43', 'cdcc54',
         'ddda27', 'ccca61', 'cbcd29', 'aacd26', 'dbcd57']

# Pedimos un número al usuario.
num_categorias = int(input('\nIngrese el número de categorías: '))

# Extraemos la parte numerica de lo elementos de 'lista'.
lista_numeros = [int(i[-2:]) for i in lista]

# Creamos una variable limite para cada categoría.
limite_fin = 1

for i in range(num_categorias):

    # Actualizamos el limite inicial y final de cada categoría.
    limite_inicio = limite_fin
    limite_fin += round(99 / num_categorias)

    # Agregamos los elementos que pertenecen a la categoría.
    elementos = [numero for numero in lista_numeros if limite_inicio <= numero < limite_fin]

    print(f'\n--- Categoría N°{i + 1}: [{limite_inicio} - {limite_fin - 1}] ----\nNúmero de elementos: {len(elementos)}\n{elementos}\n')

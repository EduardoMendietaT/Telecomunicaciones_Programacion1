'''
Se requiere un programa que dada una frase, muestre los caractéres que no se repiten. Por ejemplo:
Entrada: "esta es una cadena de texto"
Salida: "ucxo"
Sugerencia: Puede crear un diccionario que contenga como claves cada uno de los caracteres de la 
entrada y además almacene el número de ocurrencias de los mismos. Luego solo seleccionar los caracteres 
que aparezcan una sola vez
'''
# Solicitamos una frase al usuario.
frase = input('\nIngrese una frase: ')

# Transformamos todos los caracteres a minúsculas y removemos los espacios vacios.
frase = frase.replace(' ', '').lower()

# Creamos un diccionario con los caracteres de la frese como claves y el número de ocurrencias de estos como valor.
letras = dict()
for i in frase:
    if i in letras.keys():
        letras[i] += 1
    else:
        letras[i] = 1

# ESxtraemos en una lista los caracteres que apareces una sola vez.
letras_sin_repetir = [key for key, value in letras.items() if value == 1]

# Mostramos los caracteres por consola.
print(f'\nSalida: {"".join(letras_sin_repetir)}\n')
'''
Se requiere un programa que dada una frase, muestre los caractéres que no se repiten. Por ejemplo:
Entrada: "esta es una cadena de texto"
Salida: "ucxo"
Sugerencia: Puede crear un diccionario que contenga como claves cada uno de los caracteres de la 
entrada y además almacene el número de ocurrencias de los mismos. Luego solo seleccionar los caracteres 
que aparezcan una sola vez
'''
# Solución 1: --------------------------------------------------------
frase = input('\nIngrese una frase: ')

frase = frase.replace(' ', '').lower()

letras = dict()
for i in frase:
    if i in letras.keys():
        letras[i].append(i)
    else:
        letras[i] = [i]

letras_sin_repetir = [i[0] for i in letras.values() if len(i) == 1]

print(''.join(letras_sin_repetir))
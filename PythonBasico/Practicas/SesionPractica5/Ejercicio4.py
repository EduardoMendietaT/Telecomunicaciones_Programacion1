'''
Dada una cadena de texto ingresada por el usuario, crear una tupla que contenga únicamente los
caractéres sin repetición. Por ejemplo:

Entrada: "esta es una cadena de texto"
Salida: ('e', 's', 't', 'a', 'u', 'n', 'c', 'd', 'x', 'o')
'''

cadena = input('\nIngrese una frase: ')
cadena = ''.join(cadena.split())

'''
letras_no_repetidas = []

for i in cadena:
    if i not in letras_no_repetidas:
        letras_no_repetidas.append(i)


print(letras_no_repetidas)
'''

letras = []
[letras.append(i) for i in cadena if i not in letras]
print(letras)

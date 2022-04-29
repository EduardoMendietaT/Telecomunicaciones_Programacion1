'''
Dada una frase de texto, se requiere dividirla en frases cuyo separador es el '.'.
Luego, mostrar las frases en mayúsculas solo si están en una posición par
'''
frase = 'Frase 1. Frase 2. Frase 3. Frase 4. Frase 5. Frase 6'

# Creamos una lista a partir de 'frase' utilizando como separador al '.'
frases = frase.split('.')

# imprimimos las frases de la lista anterior.
i = 0
while i < len(frases):
    # Convertimos a mayúsculas y quitamos los espacio de inicio y fin si:
    # La posición es par, asumiendo que las posiciones de las listas inician en cero.
    print(frases[i].upper().strip() if i % 2 == 0 else frases[i].strip())
    i += 1

'''
Se requiere crear un programa para encriptar un mensaje. La lógica es la siguiente: 
el mensaje original será transformado moviendo las posiciones de los caracteres en base 
a la lista numérica provista. Para este ejercicio, se le debe pedir al usuario una frase 
y el pad. El pad podrá ser cualquier número de 3 cifras. Por ejemplo:

Frase: el zorro es una pelicula vieja
pad: 123
salida: fn aqusq fu vpd rhmkfvnd xlfld

Analizando la salida:
e -> f movido una posición
l -> n movido dos posiciones
“ “ -> los caracteres vacíos no se transforman
z -> a movido una posición
o -> q movido dos posiciones
r -> u movido tres posiciones

Entonces, pad es una secuencia con números que se reutiliza para el proceso. Además, las posiciones 
del alfabeto pueden verse como circulares; es decir, si se debe mover z dos posiciones, el resultado 
será b Ayuda: El siguiente código genera una lista con los caracteres de la a-z:
'''
def get_char_encript(letra, num_recorrer):
    abecedario = list(map(chr, range(97, 123)))
    for index, value in enumerate(abecedario):
        if letra == value:
            next_posc = index + num_recorrer
            num_items = len(abecedario)
            if next_posc > num_items - 1:
                return abecedario[next_posc - num_items]
            else:
                return abecedario[next_posc]
    return letra


def get_encript_text(texto, path):
    encript_text = ""
    cont = 0
    for i in texto:
        if cont == len(path):
            cont = 0
        if cont < len(path):
            encript_text += get_char_encript(i, path[cont])
        cont += 1
    return encript_text


def main():
    frase = input('\nIngrese una frase: ')
    path = input('Ingrese un path para encriptar, debe ser un numero entero de 3 cifras: ')

    frase_encriptada = get_encript_text(frase, [int(i) for i in path])

    print(f'\nLa frase encriptada es: {frase_encriptada}.\n')


if __name__ == '__main__':
    main()
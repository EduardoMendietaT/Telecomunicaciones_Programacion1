'''
Implemente un programa que dada una lista con mensajes codificados, verificar cuantas veces se repite un patrón 
en ellos. Para ello, primeramente deberá generar dichos mensajes, i.e. una lista de n mensajes donde cada 
elemento es un string de m caracteres randómicos que van desde el caracter a hasta k. Una lista de mensajes 
válida tiene la siguiente forma:

['ekjeg', 'hgkch', 'biaae', 'fcfhb', 'akcbg', 'jhdaj', 'geibk', 'ebchj', 'heeae', 'kfeid']

Para n = 10 y m = 5

Luego, buscar un patrón cualquiera de 2 caractéres en cada uno de los elementos de esta lista. El programa 
deberá retornar cuantas veces encontró el patrón en la lista. Se contabilizan únicamente los elementos que 
contenga el patrón una sola vez.

Ejemplo:
mensaje: ['keeab', 'dhabe', 'afebd', 'cabab', 'fkabi', 'kifca', 'bfiai', 'hhjbk', 'jkjij', 'echgf']
patron: ab

salida esperada: 3

Nota: para generar valores aleatorios dentro de un conjunto, se puede usar la función choice de la librería random
'''
import random

get_text = lambda lista, longitud: ''.join([random.choice(lista) for i in range(longitud)])


def get_num_ocurrencias(texto, patron):
    limt_inicial = 0
    limt_final = len(patron)
    ocurrencias = 0
    while limt_final != len(texto) + 1:
        if texto[limt_inicial:limt_final] == patron:
            ocurrencias += 1
        limt_inicial += 1
        limt_final += 1
    return ocurrencias


def main():
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    n = random.randint(10, 30)
    m = random.randint(5, 15)

    mensajes = [get_text(letras, m) for i in range(n)]
    #mensajes = ['keeab', 'dhabe', 'afebd', 'cabab', 'fkabi', 'kifca', 'bfiai', 'hhjbk', 'jkjij', 'echgf']
    patron = get_text(letras, 2)
    #patron = 'ab'

    ocurrencias = 0
    for i in mensajes:
        if get_num_ocurrencias(i, patron) == 1:
            ocurrencias += 1

    print(f'\nLista: {mensajes}\n\nEl patrón: "{patron}" aparece {ocurrencias} veces en la lista.\n') 


if __name__ == '__main__':
    main()
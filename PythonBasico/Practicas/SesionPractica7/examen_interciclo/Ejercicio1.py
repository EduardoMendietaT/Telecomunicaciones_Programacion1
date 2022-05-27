'''
Se requiere escribir un programa que dada una lista de listas conteniendo números enteros, genere una 
lista de una sola dimensión contenido todos los números. Esta operación comúnmente se conoce como 
aplanar una lista. Esta lista además, deberá ser ordenada de forma descendente. Por ejemplo:

Entrada: [[1, 12, 3], [100, 13, 22, 0], [15, 30]]
Salida: [100, 30, 22, 15, 13, 12, 3, 1, 0]

Para solucionar este ejercicio, el alumno no podrá hacer uso de ninguna función preestablecida en Python.
'''
aplanar_lista = lambda listas: [y for i in listas for y in i]


def ordenar_descendente(lista):
    for i in range(len(lista)):
        cont = 0
        while cont < len(lista) - 1:
            if lista[cont] < lista[cont + 1]:
                aux = lista[cont]
                lista[cont] = lista[cont + 1]
                lista[cont + 1] = aux
            cont += 1
    return lista


def main():
    entrada = [[1, 12, 3], [100, 13, 22, 0], [15, 30]]
    salida = ordenar_descendente(aplanar_lista(entrada))
    print(f'\nSalida: {salida}\n')


if __name__ == '__main__':
    main()
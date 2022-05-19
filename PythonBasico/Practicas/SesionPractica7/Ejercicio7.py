'''
Modifique el ejercicio anterior para que, en vez de usar definciones de funciones tradicionales 
i.e. funcion1, funcion2, y funcion3, utilice funciones lambda para implementar la misma funcionalidad
'''
funcion1 = lambda x: x**2

funcion2 = lambda x: x**3

funcion3 = lambda x: (x - 5)**2 - 2*x + 3

clasificar_por_fn = lambda fn, rango: f'\n{list(map(fn, rango))}'


def main():
    funciones = [funcion1, funcion2, funcion3]
    limite_inicio = 1
    salida = f'\nSalida:\n'

    for f in funciones:
        salida += clasificar_por_fn(f, range(limite_inicio, 31, 3))
        limite_inicio += 1

    print(f'{salida}\n')


if __name__ == '__main__':
    main()
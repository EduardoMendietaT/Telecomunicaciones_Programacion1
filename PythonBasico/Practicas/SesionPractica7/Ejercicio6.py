'''
Modifique el código del ejercico anterior para optimizarlo de forma tal que no sea necesario realizar 
iteraciones sobre x : for x in x_vals:.

Nota: utilice la función map.
'''

def funcion1(x):
    return x**2


def funcion2(x):
    return x**3


def funcion3(x):
    return (x - 5)**2 - 2*x + 3


def main():
    funciones = [funcion1, funcion2, funcion3]
    limite_inicio = 1
    salida = f'\nSalida:\n\n'

    for f in funciones:
        res = list(map(f, range(limite_inicio, 31, 3)))
        salida += f'{res}\n'
        limite_inicio += 1

    print(f'{salida}\n')


if __name__ == '__main__':
    main()
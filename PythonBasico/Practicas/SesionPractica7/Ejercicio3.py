'''
Cree y pruebe una función que dada una lista (numeros) de números enteros y un número entero (x), 
retorne 3 valores: (1) cuantos números iguales x existen; (2) cuantos números menores a x existen; y, 
(3) cuantos números mayores a x existen.

Ejemplo:

numeros: [10, 5, 4, 4, 6, 3, 7, 10]
x: 4

salida esperada: Existen 2 números iguales a 4 Existen 5 números menores a 4 Existen 1 números mayores a 4
'''
def get_mayores_menores_iguales(numeros, x):
    iguales, menores, mayores = 0, 0, 0
    for i in numeros:
        if x < i:
            mayores += 1
        elif x > i:
            menores += 1
        else:
            iguales += 1
    return iguales, menores, mayores


def main():
    numeros = [10, 5, 4, 4, 6, 3, 7, 10]
    x = input('\nIngrese un número: ')
    if x.isdigit():
        iguales, menores, mayores = get_mayores_menores_iguales(numeros, int(x))
        print(f'\nExisten {mayores} números mayores, {menores} menores y {iguales} iguales a {x}.\n')
    else:
        print('\nIngrese solo números enteros!\nFin del programa\n')


if __name__ == '__main__':
    main()
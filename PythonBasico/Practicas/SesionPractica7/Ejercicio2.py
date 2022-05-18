'''
Escribir y probar una función que genere un patrón similar a:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

def get_patron(profundidad):
    patron = ''
    linea = ''
    if profundidad % 2 != 0:
        for i in range(profundidad):
            if i > profundidad // 2:
                linea = linea[:-2]
            else:
                linea += '* '
            patron += f'\n{linea}'
    return patron


def main():
    profundidad = input('\nIngrese un número entero positivo impar: ')
    if profundidad.isdigit() and int(profundidad) % 2 != 0:
        print(f'{get_patron(int(profundidad))}\n')
    else:
        print('\nDebe ingresar un número impar!\nfin del programa!\n')


if __name__ == '__main__':
    main()
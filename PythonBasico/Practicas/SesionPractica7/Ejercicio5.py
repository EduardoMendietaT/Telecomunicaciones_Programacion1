'''
Modifique el código anterior para que se implemente una nueva función funcion3 que ejecute la siguiente 
función: (x-5)^2 - 2x + 3. Se definirán valores de x desde 1..30 y la ejecución será como sigue: primero se 
ejecutará funcion1, luego funcion2, y finalmente funcion3. funcion1 evaluará los valores de x = {1,4,7,10,...}. 
funcion2 evaluará los valores x = {2,5,8,11,...}y funcion3 evaluará los valores x = {3,6,9,12,...}. El 
programa mostrará los valores de las funciones para los números números evaluados.

Salida esperada:

[1, 16, 49, 100, 169, 256, 361, 484, 625, 784]
[8, 125, 512, 1331, 2744, 4913, 8000, 12167, 17576, 24389]
[1, -8, 1, 28, 73, 136, 217, 316, 433, 568]
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
        res = [f(i) for i in range(limite_inicio, 31, 3)]
        salida += f'{res}\n'
        limite_inicio += 1

    print(f'{salida}\n')


if __name__ == '__main__':
    main()
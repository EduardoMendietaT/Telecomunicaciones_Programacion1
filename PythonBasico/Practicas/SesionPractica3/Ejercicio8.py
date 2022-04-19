'''
Se tienen 2 listas de numeros enteros previamente ingresadas, i.e.x,y.
Se requiere crear un programa para mostrar las distintas combinaciones de elementos xi,yj
tales que (xi+yj) <= 100 y (xi*yj) % 2 == 0. Si estas condiciones no son ciertas,
la ejecucion del programa terminara.
'''
# Listas con valores previamente almacenados.
l1 = [10, 11, 30]
l2 = [2, 4, 3]

# inicializamos la variable contador para 'l1'.
cont_l1 = 0

# Variable bandera para terminar el programa:
salir = False

while cont_l1 < len(l1) and not salir:
    print('\n---------\n')
    xi = l1[cont_l1] # Extraemos el número de la posición 'cont_l1'

    cont_l2 = 0 # inicializamos la variable contador para 'l2'.
    while cont_l2 < len(l2) and not salir:
        yj = l2[cont_l2] # Extraemos el número de la posición 'cont_l2'

        # Condición para que el programa imprima la combinación xi,yj y mantenga su ejecución.
        if (xi + yj) <= 100 and (xi * yj) % 2 == 0:
            print(f'({xi},{yj})')
        else:
            salir = True
        cont_l2 += 1 # Incrementamos la variable contador.
    cont_l1 += 1 # Incrementamos la variable contador.

print(f'\nEl programa ha finalizado!\n')

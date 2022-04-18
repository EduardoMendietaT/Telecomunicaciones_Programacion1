'''
Cree un algoritmo que pida al usuario que ingrese un número, si el número ingresado es 0, el programa
termina su ejecución, caso contrario, se debe pedir nuevamente al usuario que ingrese otro número.
'''
continuar = True # Variable bandera para detener el bucle.

# Pedimos un número al usuario hasta que ingrese el cero.
while continuar:
    numero = int(input('\nIngrese un número: '))
    if numero == 0:
        continuar = False

print('\nEl programa a finalizado!\n')

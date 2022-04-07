'''
Dada una lista con colores, pedir al usuario el ingreso de un color. Mostrar cuantas veces el color 
ingresado por el usuario esta presente en la lista predeterminada.
'''
colores = ['amarillo', 'verde', 'rojo', 'azul', 'violeta', 'amarillo', 'violeta', 'amarillo']

color = input('\nIngrese un color: ')

# Verificamos cuantas veces aparece el color en la lista.
cont = 0
for i in colores:
    if color == i:
        cont += 1

print(f'\nEl color: {color}, se encuentra {cont} vez/veces en la lista.\n')
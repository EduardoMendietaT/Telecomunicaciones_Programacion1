'''
Crear un algoritmo que concatene los valores del 1 al 10 a una lista ya existente, y la muestre en pantalla
'''
# lista con valore previamente almacenados.
l = [5, 1, 9]

# Inicializamos la variable contador.
cont = 1

while cont <= 10:
    l += [cont] # Almacenamos el valor de 'cont' en una lista y la concatenamos con 'l'.
    cont += 1

print(f"\nLa lista es: {l}\n")

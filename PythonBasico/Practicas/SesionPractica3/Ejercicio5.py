'''
Modifique el código del Ejercicio 3 para optimizarlo con el uso de listas
'''
# Lista con los números que inician la serie de Fibonacci.
serie_fibonacci = [0, 1]

n = int(input("\nIngrese un número mayor a 2: "))

# Inicialización de la variable contadora.
cont = 1

# La condición hasta n-2 porque ya tenemos los dos primeros dijitos almacenados.
while cont <= n - 2:
    # Cada número de la serie es el resultado de sumar los 2 anteriores
    numero = serie_fibonacci[-1] + serie_fibonacci[-2]
    # Almacenamos el valor de 'numero' en una lista y la concatenamos con 'serie_fibonacci'.
    serie_fibonacci += [numero]
    cont += 1

print(f"\nLa serie es: {serie_fibonacci}\n")

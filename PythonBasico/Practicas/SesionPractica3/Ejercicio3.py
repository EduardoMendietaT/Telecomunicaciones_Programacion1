'''
La serie de Fibonacci es una secuencia F={f0, f1, f2,...,fn}, en donde , f0=0, f1=1, y
fi = fi-1 + fi-2 para 2 <= i <= N.

Crear un algoritmo para que, ingresado un número n > 2, mostrar los n dígitos correspondientes
a la serie de Fibonacci. Por ejemplo:

si n = 10
salida: 0 1 1 2 3 5 8 13 21 34
'''
# Números que inician la serie de Fibonacci.
f1 = 0
f2 = 1

# Almacenaremos los n dijitos de la serie.
serie_fibonacci = "0 1 "

n = int(input("\nIngrese un número mayor a 2: "))

# Inicialización de la variable contadora.
cont = 0

# La condición hasta n-2 porque ya tenemos los dos primeros dijitos almacenados.
while cont < n - 2:
    numero = f1 + f2 # Cada número de la serie es el resultado de sumar los 2 anteriores
    serie_fibonacci += f"{numero} "
    f1 = f2 # Actualizamos los números anteriores.
    f2 = numero
    cont += 1

print(f"\nLa serie es: {serie_fibonacci}\n")

'''
Escribir un programa para generar la siguiente secuencia: Se comienza con un número
x0 y el siguiente número x1  se calcula de la siguiente manera:
    - xi / 2, si, xi % 2 == 0
    - 3xi + 1, si, xi % 2 <> 0
Si xi = 1, se para la ejecucion, y la secuencia se habra construido de forma completa.
Por ejemplo, si x0 = 5, la secuencia obtenida es la siguiente:
    - 5 16 8 4 2 1
'''
n = int(input("\nIngrese un número: "))

# Lista para almacenar la secuencia de números según las condiciones
numeros = [n]

# Almacenaremos los números hasta que la secuencia llegue a 'n = 1'.
while n != 1:
    # La generacion del siguiente número depende de si 'n' es par o impar.
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    # Almacenamos a 'n' en una lista y la concatenamos la lita de números.
    numeros += [n]

print(f'\nLa secuencia es: {numeros}\n')

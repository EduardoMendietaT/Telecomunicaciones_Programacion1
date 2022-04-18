'''
La serie de Fibonacci es una secuencia F={f0, f1, f2,...,fn}, en donde , f0=0, f1=1, y
fi = fi-1 + fi-2 para 2 <= i <= N.

Crear un algoritmo para que, ingresado un número n > 2, mostrar los n dígitos correspondientes
a la serie de Fibonacci. Por ejemplo:

si n = 10
salida: 0 1 1 2 3 5 8 13 21 34
'''
n = int(input('\nIngrese un número mayor a 2: '))
print(f'\n-------- los {n} dígitos correspondientes a la serie de Fibonacci --------\n')
serie_fibonacci = '0 '

cont = 0
while cont <= n:
    cont += 1
    pass

print(f'salida = {serie_fibonacci}')

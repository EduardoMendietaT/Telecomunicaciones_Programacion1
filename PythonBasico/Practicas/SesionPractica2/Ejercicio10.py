'''
Para cada uno de los números xi tal que x = [2,...,20] imprimir los números que son divisibles para 
xi excluyendo a 1 y xi. Por ejemplo, si xi = 18, los números que lo dividen son: [2, 3, 6, 9]
'''
# Generamos una lista de números 1 -20
x = list(range(2, 21))

# Imprimimos los números para los que 'xi' es divisible excluyendo a 1 y 'xi'
for xi in x:
    cadena = f'\n{xi} es divisible para: ['
    for i in range(2, xi):
        if xi % i == 0:
            cadena += f' {i}'
    print(f'{cadena} ]\n')
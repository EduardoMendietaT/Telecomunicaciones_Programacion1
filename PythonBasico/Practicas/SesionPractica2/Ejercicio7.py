'''
Imprima los números xi tal que x = [0,...,100] y xi sea divisible para 5, pero no para 3
'''
# Generamos una lista 'x' con números de 0 a 100.
start, stop = 0, 100
x = list(range(start, stop + 1))

print('\nNúmeros divisibles para 5 pero no para 3:\n')

# imprimimos los 'xi' de 'x' que sean números divisibles para 5 pero no para 3.
for xi in x:
    if xi % 5 == 0 and xi % 3 != 0:
        print(xi)

print('\n')
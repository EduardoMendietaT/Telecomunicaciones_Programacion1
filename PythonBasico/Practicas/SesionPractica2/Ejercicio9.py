'''
Modifique el código anterior de forma que solo muestre las combinaciones de números xi,yj 
tal que xi + yj <= 20
'''
# Construimos los conjuntos x = [1,2,...,10] e y = [11,12,...,15].
x = list(range(1, 11))
y = list(range(11, 16))

print('\nPosibles combinaciones (xi, yj) tal que xi + yj <= 20:')

#Imprimimos las posibles combinaciones (xi, yj).
for xi in x:
    print('\n----\n')
    for yj in y:
        if xi + yj <= 20:
            print(f'({xi},{yj})')

print('\n')
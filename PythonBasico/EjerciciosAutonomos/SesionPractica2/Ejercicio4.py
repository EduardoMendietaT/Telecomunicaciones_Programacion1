'''
'''
print('\n----- Números pares entre 1 < x <= 30 -----\n')
for i in range(2, 31, 2):
    print(i)

print('\n----- Suma de los números impares entre 1 < x <= 30 -----\n')
suma = 0
for i in range(1, 31, 2):
    print(i)
    suma += i

print(f'La suma es: {suma}.\n')
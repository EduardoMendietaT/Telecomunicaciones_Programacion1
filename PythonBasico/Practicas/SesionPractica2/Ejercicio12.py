'''
Crear un programa que muestre la tabla de multiplicar de un número ingresado por el usuario. Por ejemplo, 
para un número x = 6 el programa debe mostrar:
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60
'''
numero = int(input('\nIngrese un número: '))
print(f'\n------ Tabla del {numero} ------\n')

# Imprimimos la tabla de multiplicar del número ingresado por el usuario.
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')

print('\n')
'''
Dados 4 números, determine cual es el número mayor entre ellos.
'''
num1 = int(input('\nIngrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
num3 = int(input('Ingrese el tercero número: '))
num4 = int(input('Ingrese el cuarto número: '))

if num1 > num2 and num1 > num3 and num1 > num4:
    num_mayor = num1
elif num2 > num3 and num2 > num4:
    num_mayor = num2
elif num3 > num4:
    num_mayor = num3
else:
    num_mayor = num4

print(f'\nEl número mayor es: {num_mayor}.\n')
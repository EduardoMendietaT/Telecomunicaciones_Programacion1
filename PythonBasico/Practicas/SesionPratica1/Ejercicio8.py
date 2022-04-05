'''
Dados 4 números, determine cual es el número mayor entre ellos.
'''
# Solicitamos 4 números por consola.
num1 = int(input('\nIngrese el valor del primer número: '))
num2 = int(input('Ingrese el valor del segundo número: '))
num3 = int(input('Ingrese el valor del tercero número: '))
num4 = int(input('Ingrese el valor del cuarto número: '))

# Validamos cuál es el mayor de los 4 números.
if num1 > num2 and num1 > num3 and num1 > num4:
    mayor = num1
elif num2 > num3 and num2 > num4:
    mayor = num2
elif num3 > num4:
    mayor = num3
else:
    mayor = num4

print(f'\nEl número mayor es: {mayor}.\n')
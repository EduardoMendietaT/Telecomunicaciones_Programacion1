'''
Para este ejercicio, pida al usuario que ingrese 3 valores numéricos y transfórmelos a valores
del tipo float luego muestre los valores transformados
'''
# Pedimos al usuario el ingreso de tres valores de tipo entero.
numero_1 = int(input('\n------ Ingrese 3 números enteros ------\n\nIngrese el primer número: '))
numero_2 = int(input('Ingrese el segundo número: '))
numero_3 = int(input('Ingrese el tercer número: '))

# Transformamos los números enteros a tipo float.
numero_1 = float(numero_1)
numero_2 = float(numero_2)
numero_3 = float(numero_3)

# Mostramos los numeros por consola.
print(f'\nLos números transformados son: [{numero_1}, {numero_2}, {numero_3}].\n')

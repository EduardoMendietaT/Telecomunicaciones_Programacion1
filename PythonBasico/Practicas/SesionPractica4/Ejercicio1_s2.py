'''
Para este ejercicio, pida al usuario que ingrese 3 valores numéricos y transfórmelos a valores
del tipo float luego muestre los valores transformados
'''
# 1. Solicitamos al usuario el ingreso de tres valores de tipo entero.
cant_numeros = 3
print(f'\n---- Ingrese {cant_numeros} números enteros ---- ')
numeros_enteros = [input(f'N°{i+1}: ') for i in range(cant_numeros)]

# 2. Transformamos los números enteros a tipo float.
numeros_flotantes = [float(i) for i in numeros_enteros]

# 3. Mostramos los numeros por consola.
print(f'\nLos números transformados son: {numeros_flotantes}.\n')

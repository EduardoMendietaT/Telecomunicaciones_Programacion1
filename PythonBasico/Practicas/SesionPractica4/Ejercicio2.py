'''
Pida al usuario que ingrese 5 valores. El programa calculará el promedio de los valores ingresados, siempre
y cuando estos sean del tipo entero.
'''
# Pedimos al usuario el ingreso de cinco números enteros.
cant_numeros = 5
print(f'\n------ Ingrese {cant_numeros} números enteros para calcular su promedio ------\n')
numeros = [input(f'N°{i}: ') for i in range(1, cant_numeros + 1)]

# Validamos que todas las entradas sean números enteros.
calcular_promedio = True
for i in numeros:
    if not i.isnumeric():
        calcular_promedio = False
        print(f'\nLa entrada: "{i}", no es un número entero, no se puede calcular el promedio.\n')
        break

# Calculamos el promedio de los números si la validacion es correcta.
if calcular_promedio:
    suma = 0
    for i in numeros:
        suma += int(i)
    print(f'\nEl promedio es: {suma/len(numeros)}\n')

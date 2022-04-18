'''
Mostrar los números impares en el rango entre 1 y 10, y al final se muestre su suma
'''
print('\n')

# 1. Usando el estamento While: ------------------------------------------------
i = 1  # inicialización del contador
suma = 0  # inicialización de la variable contadora

# Suma de los numeros impares en el rango 1 - 10
while i <=10:
    if i % 2 != 0:
        print(i)
        suma += i  # actualización de la variable acumuladora
    i += 1  # actualización del contador

print(f"\nLa suma de los números impares en el rango [1-10] es: {suma}.\n")

# 2. Usando el estamento For: ------------------------------------------------
# Suma de los numeros impares en el rango 1 - 10
suma = 0
for i in range(1, 10, 2):
    print(i)
    suma += i
print(f"\nLa suma de los números impares en el rango [1-10] es: {suma}.\n")
# El estamento for es mas eficente.

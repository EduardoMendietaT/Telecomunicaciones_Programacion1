'''
Ingrese un valor numerico x, comprovar si es positivo, negativo 0 igual a cero.
'''

x = int(input("\nIngrese un valor numérico: "))

# Validamos si x es positivo, negativo o cero.
if x > 0:
    print("\nEl valor ingresado es positivo.\n")
elif x == 0:
    print("\nEl valor ingresado es cero.\n")
else:
    print("\nEl valor ingresado es negativo.\n")
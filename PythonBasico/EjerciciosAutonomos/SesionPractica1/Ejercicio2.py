'''
Ingresar un valor por teclado y validar si es positivo, negativo o cero.
'''
x = int(input('Ingrese un valor numerico: '))

if x > 0:
    print('El valor ingresado es positivo.')
elif x == 0:
    print('El valor ingresado es 0.')
else:
    print('El valor ingresado es negativo.')
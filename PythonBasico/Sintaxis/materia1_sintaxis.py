# Programación Para Todos (Python 3)

# 1. HOLA MUNDO. ------------------------------------------------------------------------------

print(f'Hola Mundo desde Python.\n')

# 2. TIPOS DE DATOS. --------------------------------------------------------------------------
# La informacion se reprentan como datos dentro de los programas, los datos son como la materia 
# prima con la que pueden trabajar los programas.

entero = 3
real = 3.14
cadena = 'cadena de caracteres'
caracter = '3'
booleano = True # False
lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
diccionario = {'clave': 'valor'}

# 3. VARIABLES. ---------------------------------------------------------------------------------
# Espacios en la memoria principal del ordenador. Son como 'cajas' que almacenan informacion(Datos).

nombre = 'Pepe'
edad = 34

# 4. OPERADORES. --------------------------------------------------------------------------------
# Concatenación: +
# Comparación: <, >, ==, >=, <=, !=
# Lógicos: and, or, not
# Aritmeticos: +, -, *, /, %, //(cociente entero), **(potencia)
# Pertenencia: in, not in
# Identidad: is, is not 
# Asignación: +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
# }Nivel de bits: |, ^, &, <<, >>, ~

# 5. ENTRADA Y SALIDA DE DATOS --------------------------------------------------------------------
# Juego para adivinar el numero que esta pensando el usuario(Programacion secuencial linea a linea).

print('Vamos a jugar :)\nTe voy a solicitar que realices unas operaciones y luego adivinare el número\
    \nPiensa un numero!')
input('Presiona enter cuando estes listo...')
input('Multiplica ese numero por 2\nPresiona enter cuando estes listo...')
input('Sumale 10 a ese valor!\nPresiona enter cuando estes listo...')
input('Divide ese numero para 2\nPresiona enter cuando estes listo...')
input('Restale el numero inicial\nPresiona enter cuando estes listo...')
print('El numero que tienes en mente es: 5 alv!')

# Función print:
nombre = 'Pepito'
print('Hola! ',nombre, ', mucho gusto en conocerte.')
print('Hola! '+nombre+', mucho gusto en conocerte.')
print(f'Hola! {nombre}, mucho gusto en conocerte.')

nombre = input('Hola Usuario como te llamas: ')
print(f'Hola! {nombre}, mucho gusto en conocerte.')

valor_1 = input('Ingresa un numero: ')
valor_2 = input('Ingresa otro numero: ')
print(f'La suma de {valor_1} + {valor_2} = {int(valor_1) + int(valor_2)}')

# int(), float()

# 6. CONDICIONAL IF. ------------------------------------------------------------------------------

import random
secreto = random.randint(1, 10) # un numero entre 1 y 10

if secreto == 10:
    print('Bravo! es 10')
elif secreto == 1:
    print('Bravo! es 1')
else:
    print(f'Na el numero era {secreto}.')

#Anidamiento estructural es cuando tenemos una sentencia if dentro de otra.

# 7. OPERADOR TERNARIO: --------------------------------------------------------------------------

respuesta = "Te quedaste en suple" if secreto < 7 else "Pasaste el año!"
print(respuesta)
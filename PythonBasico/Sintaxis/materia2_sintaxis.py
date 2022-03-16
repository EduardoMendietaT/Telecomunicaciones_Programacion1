# 8. CICLO WHILE: -------------------------------------------------------------------------------------

contador = 0
while contador < 10:
    contador += 1
    print(f'Número: {contador}.\n')

while True:
    numero = input('Ingresa un numero entero: ')
    if numero.isdigit():
        print(f'Felicidades {numero} si es un número.')
        break # Rompe el ciclo.
    else:
        print(f'No mames {numero} no es un número entero.')

import os

os.system('clear') # comando para limpiar consola
contador = 0
while contador <= 10:
    contador += 1
    if(contador % 2 != 0):
        continue # rompe esa vuelta del bucle.
    print(f'{contador} ')

# 9. CICLO FOR: ----------------------------------------------------------------------------
# range(inicio, fin, cadaCuantoPasa)

for i in range(1, 11): #imprime desde el 1-10
    print(f'For: {i}')

print('*'*20) #imprime un string con 20 asteriscos.

for i in range(0, 11, 2): #números pares 0-10
    print(f'For: {i}')

# Cuenta regresiva usando un for:
import time
os.system('clear')
for i in range(10, -1, -1):# genera numeros desde 10-0
    os.system('clear')
    print(f'0{i}' if i<10 else i)
    time.sleep(1) #duerme el hilo por 1 segundo.
print('Nos vemos prros!\n')

#imprimir una a una las letras de una palabra:
palabra = 'Hola mundo!'
os.system('clear')
for letra in palabra:
    print(letra)

#obtener el promedio de datos proporcionados por el usuario:
os.system('clear')
total = 0
numero_datos = input('ingresa el numero total de datos que deseas promediar(enteros): ')
if numero_datos.isdigit():
    for i in range(int(numero_datos)):
        numero = input(f'Ingresa valor N°{i}: ')
        if numero.isdigit():
            total += int(numero)
    print(f'El promedio es: {total/int(numero_datos)}.')
else:
    print('Imbécil te dije que ingreses un número entero! >:v')

# 10. PROCEDIMIENTOS Y FUNCIONES: ------------------------------------------------------------
def saludo_personalizado():
    pass # permite que la funcion o procedimiento no tenga cuerpo y de esa manera no den errores.

def saludo_personalizado_2(nombre):
    print(f'Hola {nombre} como te encuentras!')

# Funcion:
def get_area_triangulo(base, altura):
    return (base * altura) / 2

# 11. ARGUMENTOS: -----------------------------------------------------------------------------
# Implementar un procedimiento que imprima un menu generico
# def menu(argumentoFuijo, *Argumento en lista, **Argumento en diccionario):

def menu(titulo, *args, **kwargs):
    print(f' -------------- {titulo} --------------')
    for i in range(len(args)):
        print(f' {i+1}) {args[i]}')
    opc = int(input(' Selecciona una opcion:'))
    if 1 <= opc <= len(args):
        print(f'Seleccionaste la opción {args[opc - 1]}')
    else:
        if 'error' in kwargs:
            print(f' {kwargs["error"]}')
        else:
            print(' Opcion no valida >:v')
menu('Operaciones Aritmeticas', 'Suma', 'Resta', 'Multiplicacion', error = 'No existe tal opción!')

# 12. FUNCION MAIN: -------------------------------------------------------------------------------------
def saludar(nombre):
    print(f'Hola {nombre}!')

def main():
    nombre = input('Dime tu nombre: ')
    saludar(nombre)

if __name__ == '__main__':
    main() #Evalua y ejecuta main como la funcion principal.
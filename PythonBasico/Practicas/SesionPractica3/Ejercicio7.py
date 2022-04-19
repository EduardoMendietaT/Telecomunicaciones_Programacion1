'''
Escriba un programa que iterativamente pida al usuario que ingrese números.
Se mostrarán en pantalla unicamente los números que se consideren correctos; para ello, se
definen las siguientes condiciones. Un número es correcto si:
    - Es divisible para 2 pero no para 10.
    - Es positivo.
    - Es menor a 100.
Para terminar el proceso de entrada de números y ejecucion del programa, el usuario debe ingresar -1
'''
# Inicializamos una lista para almacenar los números que cumplen con la condición del problema.
numeros_correctos = []

# variable bandera para controlar las iteraciones.
continuar = True
while continuar:
    numero = int(input("Ingrese un número [Digite -1 para terminar el proceso]: "))
    # Terminamos el proceso si 'numero = -1'
    if numero == -1:
        continuar = False
    # Condicion para que un número se pueda almacenar en la lista.
    if numero % 2 == 0 and numero % 10 != 0 and 0 < numero < 100:
        numeros_correctos += [numero]
        
print(f"\nLos números correctos son: {numeros_correctos}\n")

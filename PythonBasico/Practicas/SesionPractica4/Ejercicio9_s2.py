'''
El objetivo de este ejercicio es el de validar una cédula. consideraciones:
1. cada digito de la cedula se multiplica por 2 si impar o 1 si par.
2. Si el resultado de cada multiplicacion es mayor a 9, se resta 9 a este resultado.
3. Se suma todos los digitos encontrados en el paso anterior.
4. Si el ultimo dígito de la cedula es mayor a cero, debe coinsidir con el resultado de
   restar 10 - el ultimo digito del resultado del paso 3, caso contrario, se compara directamente
   con el último digito del resultado del paso 3.
'''
# Solicitamos el número de cedula al usuario.
cedula = input('\nIngrese un número de cédula para su validación: ')
mensaje_error = f'\nLa entrada "{cedula}" no corresponde a un número de cédula!\nEl programa ha finalizado!\n'

# Validamos que el numero ingresado contenga solo numero enteros positivos y tengan 10 digitos.
for i in cedula:
    if not i.isdigit() or len(cedula) != 10:
        print(mensaje_error)
        exit()

# 1. Multiplicamos cada dígito de la cédula, posicion par * 2 caso contrario por 1 y almacenamos en una lista.
#    Consideramos que las posiciones inician en cero.
nums_proceso1 = []
for i in range(len(cedula) - 1):
    resultante = int(cedula[i])
    if i % 2 == 0:
        resultante = int(cedula[i]) * 2
    # Validamos, si el resultado es mayor a 10, le restamos 9.
    nums_proceso1.append(resultante if resultante < 10 else resultante - 9)

# 2. Encontramos el número validador, resultante de sumar los número de la lista anterior.
num_validador = 0
for i in nums_proceso1:
    num_validador += i

# 3. Comparamos el ultimo dígito de la cedula con el último digito del número validador.
#    Si último digito de la cédula es cero se compara directamente, caso contrario se realiza:
#    10 - último digito del número validador y se compara.
mensaje = f'\nEl número de cédula: {cedula} '
ultimo_digito = int(cedula[-1])
digito_validador = int(str(num_validador)[-1])
if ultimo_digito == 0: # Generamos un mensaje considerando las condiciones anteriores.
    mensaje += 'es' if digito_validador == 0 else 'no es'
else:
    mensaje += 'es' if ultimo_digito == 10 - digito_validador else 'no es'

# Imprimimos el mensaje por consola.
print(f'{mensaje} válido.\n')

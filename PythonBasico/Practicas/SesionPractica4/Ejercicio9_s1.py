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

# Creamos una variable para almacenar el numero validador y otra para saber la poicion de cada digito de la cédula.
num_validador = 0
posicion = 0

# 1. Encontramos el número validador sumado los dígitos de la cedula, considerando que si la posición es par
#    el digito se multiplica por 2.
for i in cedula:
    if not i.isdigit() or len(cedula) != 10: # Validamos que la cédula tenga 10 digitos.
        print(mensaje_error)
        exit()
    if posicion < len(cedula) - 1: # Sumamos los 9 primeros dígitos.
        resultante = int(i) * 2 if posicion % 2 == 0 else int(i)
        # Validamos, si el digito es mayor a 9, le retamos 9.
        num_validador += resultante if resultante < 10 else resultante - 9
    posicion += 1

# 2. Generamos el mensaje considerando que si el ultimo digito de la cedula es cero:
#    comparamo directamente con el ultimo dígito del número validador.
#    caso contrario a 10 le restamos el ultimo dígito del número validador y comparamo.
mensaje = f'\nEl número de cédula: {cedula} '
if int(cedula[-1]) == 0:
    mensaje += 'es' if str(num_validador)[-1] == '0' else 'no es'
else:
    mensaje += 'es' if 10 - int(str(num_validador)[-1]) == int(cedula[-1]) else 'no es'

print(f'{mensaje} válido.\n') 

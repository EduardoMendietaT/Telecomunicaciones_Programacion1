'''
Ingresar Usuario y contraseña y validar, evaluar dentro de las 7am y 7pm
'''
import random

# Generamos una hora aleatoria entre las 7 y 19 horas.
hora = random.randint(7, 19)

# En el horario 07am y 07pm solicitamos usuario y contraseña para validar.
if 7 <= hora <= 19:
    
    usuario = input("\nUsuario: ")
    clave = input("Clave: ")
    
    if usuario == "admin" and clave == "password":
        print("\nInicio exitoso.\n")
    else:
        print("\nUsuario o clave incorrectos.\n")
else:
    print('\nEl sistema se abre desde las 07:00am hasta las 07:00pm.\n')

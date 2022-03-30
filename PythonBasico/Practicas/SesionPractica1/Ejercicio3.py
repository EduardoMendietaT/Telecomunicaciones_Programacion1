'''
Se requiere verificar que el usaurio y contraseña de un usuario sean los correctos.
Analizar y ejecutar el código acontinuación.
Se requiere implementar una condición extra: El usuario solo puede autenticarse 
entre 7 am y 7 pm. Implementar el código acontinuación:
'''
import random

# Generamos una hora aleatoria entre las 0 y 23 horas
hora = random.randint(0, 23)

print(f'\nHora: 0{hora}:00\n' if hora < 10 else f'\nHora: {hora}:00\n')

if 7 <= hora <= 19:
    usuario = input('Usuario: ')
    clave = input('Clave: ')
    if usuario == 'admin' and clave == 'password':
        print('Inicio Exitoso :D')
    else:
        print('Usuario o clave incorrectos!')
else:
    print('El servicio no esta disponible!\nHorario: 07:00 a 19:00!\nNos vemos...')
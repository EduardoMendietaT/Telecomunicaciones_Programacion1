''''''
import random

hora = random.randint(0, 23)

print(f'Hora: {hora}:00')

usuario = input('Usuario: ')
clave = input('Clave: ')

if usuario == 'admin' and clave == 'password' and 7 <= hora <= 19:
    print('Inicio Exitoso :D')
else:
    print('Usuario o clave incorrectos!')
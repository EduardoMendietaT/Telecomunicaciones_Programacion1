'''
Se tienen valores de precipitaciones de un sensor. Dependiendo de si la estación actual, 
se establecen rangos en los que las mediciones (mm/h) se consideran normales o anormales
'''
import random

estaciones = ['invierno', 'verano', 'otoño', 'primavera']

epoca = estaciones[random.randint(0,3)]
medicion = random.randint(0, 500)
mensaje = f'La medición fue de {medicion}mm/h'

# max_normal, max_anormal --> corresponden a los valores máximos en los que se considera una medición
# normal y anormal respectivamente.
def validar_medicion(max_normal, max_anormal):
    if 0 <=medicion <= max_normal:
        print(f'{mensaje}, se considera: Normal.\n')
    elif medicion <= max_anormal:
        print(f'{mensaje}, se considera: Anormal.\n')
    else:
        print(f'{mensaje}, se considera: Muy Anormal.\n')


print(f'\n---------- {epoca.upper()} ----------\n')

if epoca == 'invierno':
    validar_medicion(50, 100)
elif epoca == 'verano':
    validar_medicion(200, 400)
elif epoca == 'otoño':
    validar_medicion(100, 200)
else:
    validar_medicion(150, 300)
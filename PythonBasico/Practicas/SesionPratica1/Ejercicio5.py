'''
Crear categorías de medicion para las 4 estaciones y validar la categoria tomando como prueba una medida random.
'''
import random

epocas = ['Invierno', 'Verano', 'Otoño', 'Primavera']

epoca = epocas[random.randint(0, 3)] # Escogemos una estación de la lista aleatoriamente.
medicion = random.randint(0, 100) # Generamos una medición aleatoria entre 0 y 100.

print(f'\n------------------ {epoca.upper()} ------------------\n') # Imprimimos la época en letras mayúsculas.

# Verificamos la epoca y generamos un mensaje en base a los rangos de medición.
if epoca == 'Invierno':
    if 0 <= medicion <= 10:
        mensaje = 'Normal.'
    elif 0 <= medicion <= 20:
        mensaje = 'Anormal.'
    else:
        mensaje = 'Muy Anormal.' 
elif epoca == 'Verano':
    if 0 <= medicion <= 50:
        mensaje = 'Normal.'
    elif 0 <= medicion <= 75:
        mensaje = 'Anormal.'
    else:
        mensaje = 'Muy Anormal.'
elif epoca == 'Otoño':
    if 0 <= medicion <= 20:
        mensaje = 'Normal.'
    elif 0 <= medicion <= 40:
        mensaje = 'Anormal.'
    else:
        mensaje = 'Muy Anormal.' 
else:
    if 0 <= medicion <= 25:
        mensaje = 'Normal.'
    elif 0 <= medicion <= 50:
        mensaje = 'Anormal.'
    else:
        mensaje = 'Muy Anormal.'

print(f'\nLa medición fue: {medicion}mm/h, {mensaje}\n') 
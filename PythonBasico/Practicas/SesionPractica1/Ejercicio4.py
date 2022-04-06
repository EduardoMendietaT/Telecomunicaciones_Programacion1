'''
Implemente un sistema que muestre los siguientes mensajes dependiendo de la combinación de colores:
    - verde + verde --> OK
    - verde + amarillo --> OK
    - amarillo + amarillo --> Warning
    - rojo + verde --> Error
    - rojo + amarillo --> Error
    - rojo + rojo --> Critical
'''

color1 = input('\nIngrese un color [amarillo|verde|rojo]: ')
color2 = input('Ingrese otro color [amarillo|verde|rojo]: ')

# Generamos un mensaje en base a la combinación de 2 colores.
if color1 == 'rojo' and color2 == 'rojo':
    mensaje = 'Critical'
elif color1 == 'rojo' or color2 == 'rojo':
    mensaje = 'Error'
elif color1 == 'amarillo' and color2 == 'amarillo':
    mensaje = 'Warning'
else:
    mensaje = 'Ok'

print(f'\n{color1} + {color2} --> {mensaje}.\n')
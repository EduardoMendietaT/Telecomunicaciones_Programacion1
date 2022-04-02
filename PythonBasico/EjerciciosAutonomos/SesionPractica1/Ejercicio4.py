'''
1.Se tiene un panel de control con un aviso luminoso de hasta 3 colores: amarillo, 
verde, azul. Si la luz es verde, el estado del sistema es correcto; si la luz 
del sistema es amarilla, el sistema está soportando fallos; 
si la luz es roja, el sistema está en estado crítico.

2. Existen ahora 2 luces que pueden tener los mismos 3 colores. Implemente un 
sistema que muestre los siguientes mensajes dependiendo de la combinación de 
colores:
verde + verde --> OK
verde + amarillo --> OK
amarillo + amarillo --> Warning
rojo + verde --> Error
rojo + amarillo --> Error
rojo + rojo --> Critical
'''
color1 = input("Ingrese un color [amarillo|verde|rojo]: ")
color2 = input("Ingrese otro color [amarillo|verde|rojo]: ")

colores = [color1, color2]

if 'verde' in colores and 'rojo' not in colores:
    print('OK')
elif 'amarillo' in colores and color1 == color2:
    print('Warning')
elif 'rojo' in colores and color1 == color2:
    print('Critical')
elif 'rojo' in colores:
    print('Error')
else:
    print('Color Desconocido!')
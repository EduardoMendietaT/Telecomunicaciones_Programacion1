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
color1 = input("Ingrese un color [amarillo|verde|rojo]")
color2 = input("Ingrese otro color [amarillo|verde|rojo]")

'''
# Por alguna razón esto no funciona.
if color1 and color2 == 'verde' or color1 == 'amarillo' and color2 == 'verde' or color1 == 'verde' and color2 == 'amarillo':
    print('OK')
elif color1  and color2 == 'amarillo':
    print('Warning')
elif color1 and color2 == 'rojo':
    print('Critical')
else:
    print('Error')
'''
if color1 and color2 in ['amarillo', 'verde']:
    if color1 and color2 == 'amarillo':
        print('Warning')
    else:
        print('OK')
elif color1 and color2 == 'rojo':
    print('Critical')
else:
    print('Error')

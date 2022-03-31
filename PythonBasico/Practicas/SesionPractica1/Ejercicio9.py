'''
Escribir un programa para obtener la fecha del día siguiente a una fecha dada, 
Salida esperada:
    - Ingrese un año: 2016
    - Ingrese un mes [1-12]: 08
    - Ingrese un día [1-31]: 23
    - La fecha siguiente es [yyyy-mm-dd] 2016-8-24.
Tomar en cuenta años bisiesto: (años terminados en 00 deben ser divisibles para 400(seculares), resto de años para 4(No seculares)).
'''
meses_31 = (1, 3, 5, 7, 8, 10, 12)
meses_30 = (4, 6, 9, 11)

anio_str = input("\nIngrese un año: ")
mes = int(input("Ingrese un mes, [1-12]: "))
dia = int(input("Ingrese un dia, [1-31]: "))

bisiesto = int(anio_str) % 400 == 0 if anio_str[-2:] == '00' else int(anio_str) % 4 == 0
es_correcto = True # Imprime la fecha si los datos son correctos.

anio = int(anio_str) + 1 if mes == 12 and dia == 31 else int(anio_str)

if 0 < mes <= 12 and 0 < dia <= 31:
    if mes in meses_31 and dia <= 31:
        mes = mes + 1 if dia == 31 and mes != 12 else 1 if mes == 12 and dia == 31 else mes
        dia = dia + 1 if dia < 31 else  1  
    elif mes in meses_30 and dia <= 30:
        mes = mes + 1 if dia == 30 else mes
        dia = dia + 1 if dia < 30 else  1  
    else:
        if bisiesto and dia <= 29:
            mes = mes + 1 if dia == 29 else mes
            dia = dia + 1 if dia < 29 else  1
        elif dia <= 28:
            mes = mes + 1 if dia == 28 else mes
            dia = dia + 1 if dia < 28 else  1
        else:
            es_correcto = False
            mensaje = f'El mes {mes} no puede llevar {dia} dias!'
            if dia > 29:
                print(mensaje)
            else:
                print(f'\nAño no bisiesto, {mensaje}\n' if not bisiesto else f'{mensaje}')

    dia_str = f'0{dia}' if dia < 10 else f'{dia}'
    mes_str = f'0{mes}' if mes < 10 else f'{mes}'
    if es_correcto:
        print(f'\nLa fecha siguiente es [yyyy-mm-dd]: {anio}:{mes_str}:{dia_str}.\n')
else:
    print(f'\nMes: {mes} o Día: {dia}, no existe!\n')
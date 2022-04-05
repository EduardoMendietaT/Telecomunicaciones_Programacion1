'''
Escribir un programa para obtener la fecha del día siguiente a una fecha dada.
Conciderar años bisiestos.
Salida esperada:
    - Ingrese un año: 2016
    - Ingrese un mes [1-12]: 08
    - Ingrese un día [1-31]: 23
    - La fecha siguiente es [yyyy-mm-dd] 2016-8-24
'''
# Listas que contienen los meses con 30 y 31 días respectivamente.
meses_31 = [1, 3, 5, 7, 8, 10, 12]
meses_30 = [4, 6, 9, 11]

# Solicitamos año, mes y dia respectivamente.
anio = int(input('\nIngrese un año: '))
mes = int(input('Ingrese un mes [1-12]: '))
dia = int(input('Ingrese un día [1-31]: '))

# Validamos si el año es bisiesto asumiendo que el año sea divisible para 4.
es_bisiesto = anio % 4 == 0 
if es_bisiesto:
    print(f'\n ----------------- {anio} AÑO BISIESTO -----------------')
else:
    print(f'\n ----------------- {anio} AÑO NO BISIESTO -----------------')

# Variable bandera, cambia a falso si el valor del día no corresponde a un mes.
es_fecha_correcta = True

# Validamos mes[1-31] y día[1-12].
if 1 <= mes <= 12 and 1 <= dia <= 31:

    if mes in meses_31:
        dia += 1
        # Condición de frontera; en la linea anterior si el día es 31, este se convertira en 32, por tanto restamos 1.
        # Esto aplica para todas las coniciones de frontera.
        if dia - 1 == 31 and mes != 12:
            dia = 1
            mes += 1
        # Condición de frontera para el año.
        if dia - 1 == 31 and mes == 12:
            dia = 1
            mes = 1
            anio += 1
    elif mes in meses_30 and dia <= 30:
        dia += 1
        # Condición de frontera.
        if dia - 1 == 30:
            dia = 1
            mes += 1
    # Se asume que el mes es Febrero
    elif dia <= 29 and es_bisiesto:
        dia += 1
        # Condición de frontera.
        if dia - 1 == 29:
            dia = 1
            mes += 1
    elif dia <= 28:
        dia += 1
        # Condición de frontera.
        if dia - 1 == 28:
            dia = 1
            mes += 1
    else:
        print(f'\n¡El mes {mes} no puede llevar {dia} días!\n')
        es_fecha_correcta = False
    
    if es_fecha_correcta:
        # Damos formato al día y al mes.
        dia_str = dia
        mes_str = mes
        if dia < 10:
            dia_str = f'0{dia}'
        if mes < 10:
            mes_str = f'0{mes}'
        print(f'\nLa fecha siguiente es [yyyy-mm-dd]: {anio}-{mes_str}-{dia_str}.\n')
else:
    print(f'\nDia: {dia} o Mes: {mes}, ¡incorrectos!\n')
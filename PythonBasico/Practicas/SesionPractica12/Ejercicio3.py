'''
Cree y pruebe una función que convierta una fecha en formato MM/DD/YYYY a DDMMYYYY

Ejemplos:
Entrada: 12/07/1971
Salida: 07121971

La implementación deberá tener en cuenta que los valores de meses, días, años son numéricos, mayores a 0, 
y deben ser válidos. Por ejemplo, no existe un més 13, ni un día 30 si es Febrero. Además, se deberá tener 
cuenta si el año es biciesto para determinar los valores posibles para Febrero.

Nota: si el mes o día de entrada tienen la forma 0x, donde x es un entero, la fecha transformada deberá 
mantener esta forma, e.j. si día es 07, el día transformado también deberá ser 07 y no 7
'''

def es_bisiesto(anio):
    '''Verifica si un año es bisiesto.
    PARAMS
    ------
    anio : int
        año que se desea verificar.
    RETURN
    ------
    bisiesto : bool
        True si es bisiesto caso contrario False.
    '''
    assert type(anio) == int
    bisiesto = False
    if anio % 4 == 0:
        if anio % 100 == 0:
            bisiesto = True if anio % 400 == 0 else False
        else:
            bisiesto = True
    return bisiesto


def get_num_dias_mes(mes, anio):
    '''Retorna el número total de dias que posee un mes dependiendo del año.
    PARAMS
    ------
    mes : int 
        mes del cual se dea obtener el número de dias.
    anio : int
        año al cual pertenece el mes.
    RETURN
    ------
    key : int
        número de días que posee el mes.
    '''
    assert type(mes) == int and type(anio) == int
    assert 0 < mes <= 12
    # Meses clasificados de acuerdo al número de dias.
    categorias_meses = {
        29 if es_bisiesto(anio) else 28 : [2],
        30 : [4, 6, 9, 11],
        31 : [1, 3, 5, 7, 8, 10, 12]
    }
    for key, value in categorias_meses.items():
        if mes in value:
            return key


def convertir_fecha(fecha):
    '''Transforma una fecha con formato MM/DD/YYYY al formato DDMMYYYY, la fecha debe existir en el calendario.
    PARAMS
    ------
    fecha : str
        fecha que se desea cambia el formato.
    RETURN
    ------
    fecha : str
        fecha con el nuevo formato.
    '''
    # Validación de formato de entrada.
    assert type(fecha) == str and len(fecha) == 10
    assert fecha.count('/') == 2

    mes, dia, anio = fecha[0:2], fecha[3:5], fecha[6:]
    
    # Validación de tipo de dato y rango del día de acuerdo al mes.
    assert dia.isdigit() and mes.isdigit() and anio.isdigit()
    assert 0 < int(dia) <= get_num_dias_mes(int(mes), int(anio))

    fecha = dia+mes+anio
    return fecha


def main():
    fecha = input('\nIngrese una fecha con el formato "MM/DD/YYYY" (Ejm: 02/28/2000): ')
    try:
        print(f'Salida: {convertir_fecha(fecha)}.\n')
    except AssertionError:
        print('\nOpss! ha ocurrido un error: La fecha no existe o el formato es incorrecto!\n')


if __name__ == '__main__':
    main()
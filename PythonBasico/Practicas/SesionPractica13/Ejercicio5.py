'''
Cree un programa que pida al usuario una entrada del tipo num1:num2:num3-coef1:coef2:coef3, donde numi es 
un valor de tipo int y coefi es un número de tipo float.

Para este ejercicio use el estamento try ... except y asserts para capturar posibles errores de formato. 
De existir algun problema en el tipo de datos, el programa pedirá nuevamente la entrada al usuario. De 
existir un error de entrada, se mostrará un mensaje adecuado al usuario indicando el posible error. Este 
proceso se repetirá hasta que la entrada provista por el usuario esté correcta. Finalmente, el programa 
mostrará  sumatoria numi * coefi
'''

def get_sumatoria(patron):
    '''convierte un patron num1:num2:num3-coef1:coef2:coef3 en numeros números enteros y flotantes donde 
       num(i) es un entero y coef(i) es un flotante, ambos positivos.
    PARAM
    -----
    patron : str
        patron qUe contiene listas de números enteros y flotantes separadaas por un guion.
    RETURN
    ------
    sumatoria: float
        sumatoria de num(i) * coef(i)
    '''
    # Validamos que el patron tenga un unico guion.
    assert patron.count('-') == 1

    # Separamos las listas y validamos que tengan la misma longitud.
    listas = patron.split('-')
    enteros = listas[0].split(':')
    flotantes = listas[1].split(':')
    assert len(enteros) == len(flotantes)

    # Procedemos a transformar y realizar la operación de sumatoria.
    sumatoria = 0
    for i in range(len(enteros)):
        num = int(enteros[i])
        coef = float(flotantes[i])
        sumatoria += num * coef

    return sumatoria


def main():
   
    while True:
        print('\nIngrese un conjunto de numeros que tengan el siguiente formato --> ')
        entrada = input('"num1:num2:num3-coef1:coef2:coef3"(Ejm 4:5:10-4.5:3.4:0.0): ')
        try:
            print(f'\nLa sumatoria es: {get_sumatoria(entrada)}\n')
            break
        except AssertionError:
            print('\nEl formato es incorrecto, porfavor')
        except ValueError:
            print('\nCada uno de los num(i) y coef(i) deben ser numericos, por favor')


if __name__ == '__main__':
    main()
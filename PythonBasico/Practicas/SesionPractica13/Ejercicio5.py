'''
Cree un programa que pida al usuario una entrada del tipo num1:num2:num3-coef1:coef2:coef3, donde numi es 
un valor de tipo int y coefi es un número de tipo float.

Para este ejercicio use el estamento try ... except y asserts para capturar posibles errores de formato. 
De existir algun problema en el tipo de datos, el programa pedirá nuevamente la entrada al usuario. De 
existir un error de entrada, se mostrará un mensaje adecuado al usuario indicando el posible error. Este 
proceso se repetirá hasta que la entrada provista por el usuario esté correcta. Finalmente, el programa 
mostrará  sumatoria numi * coefi
'''
def main():
    entrada = input('\nIngrese un conjunto de numeros que tengan el siguiente formato --> \n"num1:num2:num3-coef1:coef2:coef3"(Ejm 4:5:10-4.5:3.4:0.0): ')
    assert entrada.count('-') == 1

    listas = entrada.split('-')
    enteros = listas[0].split(':')
    flotantes = listas[1].split(':')

    assert len(enteros) == len(flotantes)

    for i in range():
        pass

    print(listas)


if __name__ == '__main__':
    main()
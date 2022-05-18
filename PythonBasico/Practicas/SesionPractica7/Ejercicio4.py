'''
Tomando como base el ejercicio 10 de la sesión de ejercicios 5, crear una función que dado un string, 
que representa una cédula, retorne True si la cédula es válida, caso contrario que retorne False

Nota: Básese en su propia resolución del ejercicio y optimice el código lo más posible, ayudándose de 
slices, list comprehensions, etc.
'''
def get_validadores(cedula):
    digitos = [int(i) for i in cedula]
    validador = 0
    for i in range(len(digitos) - 1):
        resultante = digitos[i]
        if i % 2 == 0:
            resultante *= 2
        validador += resultante if resultante < 10 else resultante - 9
    return int(str(validador)[-1]), digitos[-1]


def validar_cedula(cedula):
    if cedula.isdigit() and len(cedula) == 10:
        digt_validador, ultm_digito = get_validadores(cedula)
        if ultm_digito == 0 and digt_validador == 0:
            return True
        if ultm_digito == 10 - digt_validador: 
            return True
    return False


def main():
    cedula = input('\nIngrese un número de cédula: ')
    if validar_cedula(cedula):
        print(f'\nEl número de cédula "{cedula}" es correcto\n')
    else:
        print(f'\nEl número de cédula "{cedula}" no es correcto!\n')


if __name__ == '__main__':
    main()
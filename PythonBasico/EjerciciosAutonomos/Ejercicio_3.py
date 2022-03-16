'''
Practica Pilas:
Desarrolle un script que solicite al usuario escribir una expresión aritmética, el programa debe indicar
si dicha expresión esta balanceada, es decir tiene la misma cantidad de paréntesis de apertura y cierre.
'''

def validar_expresion(expresion):
    pila = []
    for simbolo in expresion:
        if simbolo == '(':
            pila.append('(')
        elif simbolo == ')':
            if len(pila) > 0:
                pila.pop()
            else: 
                return False
    return len(pila) == 0

def main():
    expresion = input('Escribe una expresion matematica:')
    print(f'Correcto!' if validar_expresion(expresion) else f'Incorrecto!')

if __name__ == '__main__':
    main()
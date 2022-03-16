'''
Juego del Ahorcado:
Encontrar el nombre de alguno de los paises del continente americano.(Tiene un bug)
'''
import random, os

MAX_FALLOS = 5
paises = [
    'Antigua y Barbuda', 'Argentina', 'Bahamas', 'Barbados', 'Belice', 'Bolivia', 'Ecuador', 'Colombia', 
    'Chile', 'Peru', 'Brasil', 'Canada', 'Estados Unidos', 'Mexico', 'Guatemala', 'Nicaragua', 
    'Honduras', 'Costa Rica', 'Venezuela', 'Uruguay', 'Paraguay'
]

def seleccionar_pais():
    pais = random.choice(paises) #Toma un elemnto random de esa lista.
    secreto = '_' * len(pais)
    return pais, secreto # Puedo retornar mas de un valor.

def reemplazar_simbolo(pais, secreto, simbolo):
    cantidad = pais.count(simbolo)
    inicio = 0
    for i in range(cantidad):
        posicion = pais.find(simbolo, inicio)
        secreto = secreto[:posicion] + simbolo + secreto[posicion+1:]
        inicio = posicion + 1
    return secreto

def ahorcado():
    print(f'------------------------ JUEGO DEL AHORCADO ------------------------\
        \nLa palabra secreta sera el nombre de uno de los {len(paises)} del continente americano.\
        \nTienes la oportunidad de fallar hasta {MAX_FALLOS} veces.\n ¡Comencemos!')
    input('¡Presiona enter para iniciar!')
    original, secreto = seleccionar_pais()
    fallos = 0
    os.system('clear')
    while secreto != original and fallos < MAX_FALLOS:
         print(f'Palabra: {secreto}')
         s = input('¿Cuál es el símbolo que deseas destapar?')
         if s in original:
             secreto = reemplazar_simbolo(original, secreto, s)
             print(f'Bien hecho!')
         else:
             fallos += 1
             print(f'Ups! te quedan: {MAX_FALLOS - fallos} intento(s)!')
    print(f'felicidades el país es: {original}' if secreto == original else f'AHORCADO! jaja el país era: {original}')

def main():
    ahorcado()

if __name__ == '__main__':
    main()
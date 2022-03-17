'''
Script que permita al usuario registrar eventos en su agenda; Cada evento se agregara a una cola de 
prioridad de forma tal que aquellos con mayor prioridad salgan primero de la estructura. para manejar 
la ajenda se le mostrara al usuario, un menú con las opciones de agragar evento y atender evento.
'''
import os, queue

AGENDAR = 1
ATENDER = 2
SALIR = 0

def menu():
    os.system('clear')

    print(f''' ----------------------- AGENDA -----------------------
    \n {AGENDAR}) Agendar.\n {ATENDER}) Atender. \n {SALIR}) Salir.''')

def agendar_evento(agenda):
    evento = input(' ----------- Agendar Evento -----------\n Evento: ')
    agenda.put(evento)

def atender_evento(agenda):
    print(' ----------- Atender Evento -----------')
    print(' No hay eventos por atender.' if agenda.empty() else f'Evento: {agenda.get()}')

def main():
    agenda = queue.PriorityQueue()
    continuar = True
    while continuar:
        menu()
        opcion = int(input('Selecciona una opcion: '))
        os.system('clear')
        if opcion == AGENDAR:
            agendar_evento(agenda)
        elif opcion == ATENDER:
            atender_evento(agenda)
        elif opcion == SALIR:
            continuar = False
        else:
            print('Opcion no valida!')
        input('Presiona enter para continuar...')
    print('Nos vemos! :v')

if __name__ == '__main__':
    main()      
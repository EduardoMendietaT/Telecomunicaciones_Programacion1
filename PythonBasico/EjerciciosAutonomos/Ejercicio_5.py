''' Script que implemente una agenda de contactos haciendo uso de diccionarios las llaves seran 
los nombres de los contactos y como valor una tupla con el numero de telefono y el diccionario.'''
import os

SALIR = 0
AGREGAR = 1 
MOSTRAR = 2
BUSCAR = 3
MODIFICAR = 4
ELIMINAR = 5

def mostrar_menu():
    os.system('clear')
    print(f'1) Agregar contactos.\n2) Mostrar contactos.\n3) Buscar contacto.\n4) Modificar contacto.\
        \n5) Eliminar contacto.\n0) Salir.')

def agregar_contacto(agenda):
    os.system('clear')
    nombre = input('--------------------------- Agregar Contacto ---------------------------\nNombre: ')
    if agenda.get(nombre):
        print('Ya existe el contacto!')
    else:
        telefono = input('Teléfono: ')
        email = input('email: ')
        agenda.setdefault(nombre, (telefono, email))
        print('Contacto agregado con exito!')


def mostrar_contactos(agenda):
    os.system('clear')
    print('--------------------------- Mostrar Contacto ---------------------------') 
    if len(agenda) > 0:
        cont = 0
        for contacto, datos in agenda.items():
            cont += 1
            print(f'{cont}) Nombre: {contacto}, Teléfono: {datos[0]}, Correo: {datos[1]}.')
    else:
        print('No hay contactos registrados!')

def buscar_contacto(agenda):
    os.system('clear')
    print('--------------------------- Buscar Contacto ---------------------------') 
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        encontrados = 0
        for contacto, datos in agenda.items():
            if nombre in contacto:
                encontrados += 1
                print(f'{encontrados}) Nombre: {contacto}, Teléfono: {datos[0]}, Correo: {datos[1]}.')
        if encontrados == 0:
            print('No se encontro el contacto!')
    else:
        print('No hay contactos registrados!')


def modificar_contacto(agenda):
    os.system('clear')
    print('--------------------------- Modificar Contacto ---------------------------') 
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        if agenda.get(nombre):
            datos = agenda.get(nombre)
            print(f'Información Actual:\n Nombre: {nombre}, Teléfono: {datos[0]}, Correo: {datos[1]}.')
            telefono = input('\nIngresa los nuevos Datos.\nTeléfono: ')
            email = input('email: ')
            agenda[nombre] = (telefono, email)
        else:
            print('No existe el contacto')
    else:
        print('No hay contactos registrados!')


def eliminar_contacto(agenda):
    os.system('clear')
    print('--------------------------- Eliminar Contacto ---------------------------') 
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        if agenda.get(nombre):
            agenda.pop(nombre)
            print('Eliminado con exito!')
        else:
            print('No existe el contacto!')
    else:
        print('No hay contactos registrados!') 
    
def main():
    continuar = True
    agenda = {}
    while continuar:
        mostrar_menu()
        opc = int(input('Selecciona una opción: '))
        if opc == AGREGAR:
            agregar_contacto(agenda)
        elif opc == MOSTRAR:
            mostrar_contactos(agenda)
        elif opc == BUSCAR:
            buscar_contacto(agenda)
        elif opc == MODIFICAR:
            modificar_contacto(agenda)
        elif opc == ELIMINAR:
            eliminar_contacto(agenda)
        elif opc == SALIR:
            continuar = False
        else:
            print('Opcion no valida!')
        input('Presiona enter para continuar...')
    print('Nos vemos!')

if __name__ == '__main__':
    main()
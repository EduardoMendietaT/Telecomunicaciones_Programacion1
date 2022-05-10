'''
Se requiere la creación de un programa para manejar la ubicación de unos robots en una localización geográfica. 
Se asume que la ubicación geográfica está subdividida en varias zonas que tienen un identificador único. 
Para inicializar el estado de los robots, el programa aceptará una cadena de texto con el siguiente formato:
    <idRobot1>:<idUbicacion>,<idRobot2>:<idUbicacion>,...,<idRobotN>:<idUbicacion>

Posteriormente, se le pedirá al usuario la identificación de una ubicación y el programa mostrará cuantos robots 
se encuentran actualmente en esa zona. Por ejemplo:
Inicialización: 001:a001,002:a001,003:b001,004:a001,005:b002,006:b003
Entrada: "a001"
Salida: "En la zona a001 existen 3 robots"
'''
# Creamos un diccionario para almacenar "ubicación": [robots]
robots = dict()

print('\n--------------- Añadiendo Robots ---------------')

while True:

    # Solicitamos los robot con su ubicacion al usuario.
    robot = input('\nIngrese el id del Robot y su ubicación(Ejm: 001:a001): ')
    continuar = input('Ingrese "no", para dejar de agregar: ')

    # Separamos el id del robot y su ubicación.
    robot_ubic = robot.split(':')

    # Llenamos el diccionario, utilizamos la ubicación como llave y el robot como su valor.
    if robot_ubic[-1] in robots.keys():
        robots[robot_ubic[-1]].append(robot_ubic[0])
    else:
        robots[robot_ubic[-1]] = [robot_ubic[0]]

    # El usuario debera ingresar "no" para romper el bucle.
    if continuar.lower() == 'no':
        break

print('\n--------------- Buscando Robots ---------------')

# Solicitamos una ubicación al usuario.
id_ubucacion = input('\nInfrese el id de la ubicación(Ejm: a001): ')

# Si la ubicación existe obtenemos el número de robots que se encuantran en la zona y mostramos en pantalla.
if id_ubucacion in robots.keys():
    num_robots = len(robots[id_ubucacion])
    mensaje = f'\nEn la zona {id_ubucacion} existen {num_robots}'
    print(f'{mensaje} robots.\n' if num_robots != 1 else f'{mensaje} robot.\n')
else:
    print(f'\nLa ubicación: "{id_ubucacion}", no existe!\n')
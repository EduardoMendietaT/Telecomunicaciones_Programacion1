'''
Volver a la página https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat 
y revisar los contenidos restantes del tutorial (desde sensing the environment hasta el final). 
Luego, Generar un programa para jugar a "piedra, papel, o tijera". Para ello, el programa deberá 
pedir al usuario una opción; esta será leída a través del joystick: izquierda-> piedra, arriva -> papel, 
derecha -> tijera. Luego el programa seleccionará una opción aleatoriamente y verificar quien ganó para 
ese round y lo anunciará en la pantalla. Adicionalmente, en la consola se deberá ir mostrando cuantas 
veces el usuario a ganado vs el número de partidas.
'''
from sense_hat import SenseHat
import random
import time

sense = SenseHat()

colores = {'blanco': (255, 255, 255), 'negro': (0, 0, 0)}

b = colores['blanco']
n = colores['negro']

piedra = [
  b, b, b, b, b, b, b, b,
  b, b, n, n, n, n, b, b,
  b, n, n, n, n, n, n, b,
  b, n, n, n, n, n, n, b,
  b, n, n, n, n, n, n, b,
  b, n, n, n, n, n, n, b,
  b, b, n, n, n, n, b, b,
  b, b, b, b, b, b, b, b
]

papel = [
  b, b, b, b, b, b, b, b,
  b, n, n, n, n, n, n, b,
  b, n, n, n, n, n, n, b,
  b, n, n, n, n, n, n, b,
  b, n, n, n, n, n, n, b,
  b, n, n, n, n, n, n, b,
  b, n, n, n, n, n, n, b,
  b, b, b, b, b, b, b, b
]

tijera = [
  b, b, b, b, b, b, b, b,
  n, n, n, b, n, n, n, b,
  n, b, n, b, n, b, n, b,
  n, n, n, b, n, n, n, b,
  b, b, n, b, n, b, b, b,
  b, b, b, n, b, b, b, b,
  b, b, n, b, n, b, b, b,
  b, n, b, b, b, n, b, b
]

vs = [
  b, b, b, b, b, b, b, b,
  n, b, b ,n, b, n, n, n,
  n, b, b, n, n, b, b, b,
  n, b, b, n, b ,n, n, n,
  b, n, b, n, n, b, b, n,
  b, b, n, b, b, n, n, n,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]

elementos = ['piedra', 'papel', 'tijera']
elementos_juego = {elementos[0] : piedra, elementos[1] : papel, elementos[2] : tijera}

mensajes = {
  'info': 'Selecciona: izquierda - piedra, arriba - papel,derecha - piedra.',
  'gana': 'Tu ganas! :D', 
  'pierde': 'Haz perdido! :c', 
  'empate': 'Es un empate! :v'
}


def mostrar_mensaje(mensaje):
  sense.show_message(mensaje, text_colour=colores['negro'], back_colour=colores['blanco'], scroll_speed=0.15)


def resultado_partida(e_usuario, e_maquina):
  partida_ganada = False
  mensaje = ''
  if e_usuario == e_maquina:
    mensaje = mensajes['empate']
  elif e_usuario == elementos[0] and e_maquina == elementos[2] or e_usuario == elementos[2] and e_maquina == elementos[1] or e_usuario == elementos[1] and e_maquina == elementos[0]:
     mensaje =  mensajes['gana']
     partida_ganada = True
  else:
     mensaje =  mensajes['pierde']
  return mensaje, partida_ganada


def get_elemento_aleatorio():
  posicion = random.randint(0, 2)
  return elementos[posicion]


def mostrar_elementos(e_usuario, e_maquina):
  sense.set_pixels(elementos_juego[e_usuario])
  time.sleep(1)
  sense.set_pixels(vs)
  time.sleep(1)
  sense.set_pixels(elementos_juego[e_maquina])
  time.sleep(1)
 
  
def jugar(e_usuario):
  puntos = 0
  e_maquina = get_elemento_aleatorio()
  mostrar_elementos(e_usuario, e_maquina)
  mensaje, partida_ganada = resultado_partida(e_usuario, e_maquina)
  if partida_ganada:
    puntos = 1
  mostrar_mensaje(mensaje)
  return puntos
  
  
def main():
  imprimir_mensaje = True
  partidas = 0
  puntos = 0
  while True:
    if imprimir_mensaje:
      print(mensajes['info'])
      imprimir_mensaje = False
    for event in sense.stick.get_events():
      if event.action == 'pressed':
        if event.direction == 'up':
          partidas += 1
          puntos += jugar(elementos[1])
          print('\nResultado: {}/{}.\n'.format(puntos, partidas))
        elif event.direction == 'left':
          partidas += 1
          puntos += jugar(elementos[0])
          print('\nResultado: {}/{}.\n'.format(puntos, partidas))
        elif event.direction == 'right':
          partidas += 1
          puntos += jugar(elementos[2])
          print('\nResultado: {}/{}.\n'.format(puntos, partidas))
  

main()
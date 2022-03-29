'''
Se requiere conocer el modo de funcionamiento de una máquina en base a su consumo de energía.
Si la maquina consume  entre 0 y 3 watts, la máquina esta en modo reposo. Si la máquina consume 
entre 3 y 10 watts, esta en modo warmup. Si la maquina consume entre 10 y 100 watts, esta en modo
de trabajo. Si la maquina consume mas de 100 watts, se debe mostrar un mensaje de alerta debido a 
que este valor se considera anomalo.
'''
import random

consumo = random.randint(0, 150)
estado = ''

if  consumo <= 3:
    estado = 'Reposo'
elif consumo <= 10:
    estado = 'Warm up'
elif consumo <= 100:
    estado = 'Trabajo'
else:
    estado = 'Anomalo'

print(f'El consumo es: {consumo}, el estado de la máquina es {estado}.')
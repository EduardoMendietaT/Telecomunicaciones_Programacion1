'''
Se requiere saber el valor a pagar a un empleado: si las horas trabajadas son menores o
iguales a 40, se le pagara el valor por hora normal. Si las horas trabajadas exceden el valor
de 40, se le pagarán las 40 horas con el valor normal por hora, pero el excedente con un valor
equivalente a 1.5 veces el valor normal por hora.(Revisar)
'''

import random

# Valor normal de pago por hora.
usd_normal = 8

horas_trabajadas = random.randint(1, 60)
valor_pagar = 0

if horas_trabajadas > 40:
    horas_extras = horas_trabajadas - 40
    valor_pagar = (horas_extras * usd_normal * 1.5) + (40 * usd_normal)
else:
    valor_pagar = horas_trabajadas * usd_normal

print(f'El valor total por haber trabajado {horas_trabajadas} horas = ${valor_pagar}.')
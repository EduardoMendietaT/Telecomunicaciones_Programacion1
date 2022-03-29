'''
Ejercicio sobre if's anidados. Mejorar el código propuesto.
En el ejercicio anterior, ¿como se podrían eliminar los else del segundo nivel 
de indentación?
'''

import random

# Lunes --> 0, Domingo --> 6.
dia_actual = random.randint(1, 6)
hora_actual = random.randint(0, 23)
costo = 0

# Codigo propuesto: *********************************
if dia_actual < 5:
    if hora_actual < 20:
        costo = 9
    else:
        costo = 8
else:
    if hora_actual < 20:
        costo = 8
    else:
        costo = 7
print(f"Propuesto: Dia: {dia_actual}, hora: {hora_actual},El costo de la energía\
 es: ${costo}")

# Posibles soluciones: *******************************
# Solución 1:
if dia_actual < 5:
    costo = 9 if hora_actual < 20 else 8
else:
    costo = 8 if hora_actual < 20 else 7
print(f"Solución 1: Dia: {dia_actual}, hora: {hora_actual},El costo de la energía\
 es: ${costo}")

# Solución 2:
costo = 9
if dia_actual < 5:
    costo -= 1
    if hora_actual < 20:
        costo = 9
else:
    costo -= 2
    if hora_actual < 20:
        costo = 8
print(f"Solución 2: Dia: {dia_actual}, hora: {hora_actual},El costo de la energía\
 es: ${costo}")

# Solución 3:
costo = 9
if dia_actual < 5:
    if hora_actual >= 20:
        costo -= 1
else:
    costo -= 1
    if hora_actual >= 20:
        costo -= 1
print(f"Solución 3: Dia: {dia_actual}, hora: {hora_actual},El costo de la energía\
 es: ${costo}")

# Solución 4:
costo = 9
if dia_actual < 5:
    if hora_actual >= 20: costo -= 1
else:
    costo = costo - 2 if hora_actual >= 20 else  costo - 1

print(f"Solución 4: Dia: {dia_actual}, hora: {hora_actual},El costo de la energía\
 es: ${costo}")

# Solución Profe: ***********************************
if dia_actual < 5:
    costo = 8
    if hora_actual < 20:
        costo = 9
else: # fin de semana
    costo = 7
    if hora_actual < 20:
        costo = 8
print(f"Solución Profe: Dia: {dia_actual}, hora: {hora_actual},El costo de la energía\
 es: ${costo}")
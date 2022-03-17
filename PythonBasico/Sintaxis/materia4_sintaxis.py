# 15. PILAS: ----------------------------------------------------------------------------------------
# Primer elemento en entrar es el ultimo en salir.
# En python no existe un módulo para pilas.
# Buscar EjerciciosAutonomos/Ejercicio_3.py ejercicio para simular una pila y ver sus usos.

# 16. COLAS: ----------------------------------------------------------------------------------------
# Primer elemento que entra es el primero en salir.
# Se utilizan mucho con programacion asíncrona. 
# Buscar EjerciciosAutonomos/Ejercicio_4.py ejercicio uso de colas.
import queue
from re import A
cola = queue.Queue()
cola.put(5)
cola.put([2,3,4])
cola.get() #Regrasa un elemento en el orden que entraron.

# Cola de prioridad. Python ordena los elemntos en orden de prioridad, menor a mayor.
cp = queue.PriorityQueue()
cp.put(4)
cp.put(1)
cp.put(3)
cp.get() #Regresara los elemntos en este orden: 2, 3, 4.

# 17. TUPLAS: ----------------------------------------------------------------------------------------
# A diferencia de las listas las tuplas son inmutables.

tupla = (1, 2, 3, 'Hola')
tupla = 1, # Una tupla de un solo elemento.
tupla += (1, 2, 3)
tupla[2] #No se pueden hacer asignaciones.
tupla += ([9, 11],)
tupla[4][1] = 10
len(tupla)
4 in tupla
tupla.index(1)

tupla = (1, 5, 'hola')
x, y, saludo = tupla # Desempaquetado de tuplas.

print(tupla)

# 17. CONJUNTOS: ----------------------------------------------------------------------------------------
# A diferencia de las listas los conjuntos no pueden tener elementos repetidos.
A = set()
A = {0,2,3}
A.add(4)
A.add(0) # Como el 0 ya existe en el conjunto, no lo va a agregar nuevamente.
A.pop() # Elimina el primer elemento del conjunto
A.remove(2) #donde 0 es un elemento del conjunto, marca error sin no encuentra el elemento.
A.discard('Perro') #Elimina el elemento si es que existe.
0 in A
len(A)

# Operaciones con cojuntos: ******************************
A = {0,1,3,5}
B = {0, 2, 4, 6}

A & B # Devuelve un conjunto con la interseccion de estos.
A | B # Devuelve un conjunto con la union de los conjuntos sin elementos repetidos.
A - B # Devuelve un conjunto con los elementos que estan en A y no en B.
A ^ B # Devuelve un conjunto con la union de A - B y B - A.
A > B # Devuelve True si A es superconjunto(Contiene a B) de B.
A < B # Devuelve True si A es subconjunto de B.
A.isdisjoint(B) # Devuelve True si A y B no comparten elementos.
len(set('Hola mundo!'))# convierte a conjunto esa cadena y retorna su longitud.

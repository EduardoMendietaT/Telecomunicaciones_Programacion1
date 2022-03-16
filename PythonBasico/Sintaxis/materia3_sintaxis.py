# 13. LISTAS. --------------------------------------------------------------------------------
# Se pueden tener distintos tipos de datos a diferencia de otros lenguajes.

lista = []

# Agregar Elementos: *****************
lista.append(3)
lista += [1, 2, 3]
lista.extend([7, 8, 9])
lista.insert(1, 33) # POsicion, valor
lista.insert(-55, 2) # Python valida y lo coloca en la primera posicion.
lista[3] = 4

# Obtener Elementos: *****************
lista[-1] # Retorna el ultimo elemento.
lista[2]

# Eliminar Elementos: *****************
lista.pop() #retorna el ultimo elemnto y luego lo elimina.
lista.pop(2)#posición.
lista.remove(3) # Elimina el elemnto pasado por parametro, asegurarse de que exista ese valor.

# Saber si un elementos esta en la lista: *****************
3 in lista
lista.index(8)#Devuelve la posicion del elemento
lista.index(8, 2)#Busca el indice del elemnto 8 a partir del indice 2.
lista += [0, 3, 3, 3]
lista.count(3)#Devuelve el numero de veces que se repite el elemento.

# Ordenar listas: *****************
lista.sort()#orden de menor a mayor. Funciona solo si la lista es ordenable y del mismo tipo.

# Limpiar la lista: *****************
lista.clear()
lista = []
lista = [0, 1, 2, 3, -1]
len(lista)#Devuelve la cantidad de elmentos que tiene la lista.
min(lista)#Devuelve el elemento menor.
max(lista)#Devuelve el elemento mayor.
#help(list)# devuelve la documentacion de python para listas.

# Copiando listas: ******************
l1 = [0]*10 #Lista con 10 veces el valor de cero.
l2 = l1#Tanto l1 como l2 apuntan a la misma lista(por referencia)
l3 = l1.copy()#Crea una copia independiente de l1.
# Slices ****************************
l4 = l1[:] #Crea una copia independiente de l1.
l5 = l1[2:] #Toma los elementos desde la posicion 2 hasta el fin
l5 = l1[:5] #Toma los elementos desde la posicion 0 hasta 5
l5 = l1[2:7] #Toma los elementos desde la posicion 2 hasta 7
l5 = l1[2:6:2] #Toma los elementos desde la posicion 2 hasta 7 de 2 en 2

# Otras curiosidades: ****************
lista = [i for i in range (7)] #Llena la lista con elemntos desde el 0 al 6
lista2 = [i**2 for i in range(10)] #Llena la lista con los cuadrados desde 0 a 9

import random
aleatorios = [random.randint(1, 10)] * 20 #llena con 20 veces el numero random
aleatorios = [random.randint(1, 10) for i in range(10)] #llena con 10 numeros aleatorios.

matriz = [[1,2,4], [3,5,6], [2,8,6]]
matriz[0][0] #Devuelve el elemento de la posicion 0,0, se pueden crear matrices de n dimendiones.

# 14. CADENAS: ----------------------------------------------------------------------------------------

cadena = 'hola mundo!'
cadena[3]
len(cadena)
#Se puede utilizar slices. Operaciones basicas de listas tmbn se pueden hacer con cadenas.
cadena.count('o')
cadena.find('!')# encuentra la posicion de la primera coincidencia.
cadena.find('xls')# retorna -1 si no existe dentro de la cadena.
cadena.index('o')
cadena.index('o', 5)#Busca a partir de la posición 5.
'x' in cadena #Retorna True | False.
lista = ['Jose', 'Ruben', 'Pepito']
','.join(lista)#Retorna una cadena separada con comas.
','.join(cadena)
cadena.lower()
cadena.upper()
cadena.capitalize()
cadena.isdecimal()
cadena.isdigit()
cadena.isupper()
cadena.replace('o', 'O')#Cambia las 'o' por 'O'
cadena.replace('o', 'O', 1)#Cambia solo la primera coincidencia
#Las cadenas son inmutables, no se puede cambiar por asignacion, es decir(cadena[2] = 'O') esto no se puede hacer.
cadena.split[' '] #Regresa una lista con palabras que fueron separadas por el espacio.
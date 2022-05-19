'''
Implemente un programa que dada una lista con mensajes codificados, verificar cuantas veces se repite un patrón 
en ellos. Para ello, primeramente deberá generar dichos mensajes, i.e. una lista de n mensajes donde cada 
elemento es un string de m caracteres randómicos que van desde el caracter a hasta k. Una lista de mensajes 
válida tiene la siguiente forma:

['ekjeg', 'hgkch', 'biaae', 'fcfhb', 'akcbg', 'jhdaj', 'geibk', 'ebchj', 'heeae', 'kfeid']

Para n = 10 y m = 5

Luego, buscar un patrón cualquiera de 2 caractéres en cada uno de los elementos de esta lista. El programa 
deberá retornar cuantas veces encontró el patrón en la lista. Se contabilizan únicamente los elementos que 
contenga el patrón una sola vez.

Ejemplo:
mensaje: ['keeab', 'dhabe', 'afebd', 'cabab', 'fkabi', 'kifca', 'bfiai', 'hhjbk', 'jkjij', 'echgf']
patron: ab

salida esperada: 3

Nota: para generar valores aleatorios dentro de un conjunto, se puede usar la función choice de la librería random
'''
import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

n = random.randint(5, 20)
m = random.randint(3, 10)

mensajes = [''.join([random.choice(letras) for i in range(m)]) for i in range(n)]

patron = ''.join([random.choice(letras) for i in range(2)])

for i in mensajes:
    pass
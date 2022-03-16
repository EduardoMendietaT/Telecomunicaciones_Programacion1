'''
Sumar 2 matrices cuadradas generadas aleatoriamente. Utilizar comprensión de listas para generar
las matrices de forma aleatoria.
'''
import random 

N = 3
print(f' Programa que genera la suma de matrices {N}x{N}')

matriz_1 = [[random.randint(10, 50) for i in range(N)] for j in range(N)]
matriz_2 = [[random.randint(10, 50) for i in range(N)] for j in range(N)]
matriz_resultado = [[0]*N for i in range(N)]

#Realizar Operaciones
'''for fila in range(N):
    for columna in range (N):
        matriz_resultado[fila][columna] = matriz_1[fila][columna] + matriz_2[fila][columna]'''
matriz_resultado = [[matriz_1[i][j]+matriz_2[i][j] for j in range(N)] for i in range(N)]

#Imprimir: 
'''for i in range(N):
    if i == 1:
        print(f' {matriz_1[i]} + {matriz_2[i]} = {matriz_resultado[i]}')
    else:
        print(f' {matriz_1[i]}   {matriz_2[i]}   {matriz_resultado[i]}')'''
for i in range(N):
    print(f' {matriz_1[i]} + {matriz_2[i]} = {matriz_resultado[i]}' if i == N//2 else f' {matriz_1[i]}   {matriz_2[i]}   {matriz_resultado[i]}')
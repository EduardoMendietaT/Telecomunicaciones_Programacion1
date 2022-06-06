'''
Los slices son una de las funcionalidades más importantes que proveen los arrays de numpy. 
Estos posibilitan la selección de elementos de forma ágil y eficiente. De otro modo, se tendría 
que escribir mucho código, incrementando la posibilidad de crear errores y puntos de ineficiencia 
en el código.

Cuando se usan arrays de numpy, los mismos conceptos de slices de listas se aplica. Se requiere, 
dado un array de números enteros, seleccionar los siguientes elementos:

el primer y último elemento
todos los elementos excepto el último
todos los elementos excepto los 2 últimos elementos
los elementos ubicados en posiciones pares en la lista
Entrada: [ 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20]

Salidas:
[1, 20]
[ 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19]
[ 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18]
[ 2 4 6 8 10 12 14 16 18 20]
'''
import numpy as np

x = np.arange(1, 21, 1)
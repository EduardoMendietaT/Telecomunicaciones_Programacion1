'''
Numpy permite leer valores desde archivos de texto a través de la función genfromtxt. 
La estructura del archivo de texto puede verse como elementos separados, normalmente, por comas. 
Esta función transforma los elementos del archivo a una matriz de n x m donde n representa el número 
de filas y m el número de columnas. Por ejemplo, para leer un archivo se ejecuta

x = np.genfromtxt(open("archivo.csv", encoding='utf-8-sig'), delimiter=",")

el parámetro encoding es importante ya que muchas veces, dependiendo del sistema operativo, los 
caractéres de texto no se leen correctamente.

Se necesita un programa para calcular valores característicos de calificaciones de estudiantes. 
Para ello, el archivo calificaciones.csv tiene valores numéricos en 3 columnas. Cada fila del a
rchivo representa las notas de un estudiante; además, cada columna representa las calificaciones de 
los estudiantes en una prueba. Todas las calificaciones son sobre 10 puntos. Se requiere calcular el 
valor promedio de pruebas por cada estudiante; además, esta calificación deberá ser escalada a una sobre 
20 puntos. Este vector con las calificaciones deberá ser enviado a la función mostrar_notas(x) para que 
se genere un histograma de las mismas. Más información sobre el histograma al final el ejercicio.

También se deberá mostrar lo siguiente:

Número total de estudiantes
Nota promedio del curso (sobre 20 puntos)
Nota más alta
Nota más baja
Nota: para este ejercicio se deben utilizar las funciones de numpy, así que no se permite el uso de for o 
while para calcular los valores.

Un histograma muestra información sobre la frecuencia en que los valores dados en un array están en un 
cierto rango. Para el ejemplo anterior, existen 3 estudiantes cuyo promedio está entre 2.5 y 3.5. Así 
como la mayoría de alumnos tiene un promedio entre 16 y 17.5
'''
import numpy as np
import matplotlib.pylab as plt


def mostrar_notas(x):
    """
    Muestra un histograma en base a las notas ingresadas en el array `x`
    :param x: np.array, array con las notas de los estudiantes
    """
    plt.hist(x)
    plt.show()
'''
Las máscaras son arrays booleanos de numpy que permiten seleccionar elementos especificos dentro de 
otros arrays. Analice cuidadosamente el siguiente ejemplo:

# se definen 2 vectores con valores
x = np.array([1, 3, 5, 33, 8, 22, 45, 29])
y = np.array([11, 33, 55, 333, 8, 222, 45, 299])

# se crea una mascara para determinar las posiciones de los valores en `x` y `y` que cumplen las condiciones:
# x > 20 y y > 50. En `m` se tiene un array de valores booleanos donde unicamente habra valores True en las 
# posiciones que cumplan con la/las condiciones planteadas
m = (x > 20) & (y > 50)
print(m)  # se muestra el contenido del array

# se muestran los valores seleccionados por la mascara
print(np.column_stack([x[m], y[m]]))


Se requiere un programa para determinar valores anomalos en una instalación industrial. Esta instalación 
tiene mediciones de humedad y temperatura tomadas cada hora durante varios meses. Un valor se considera 
anómalo cuando su temperatura es menor a 10 gradosy su humedad es mayor a 90%. Los valores de las lecturas 
están en el archivo hum-temp.csv donde la primera columna tiene los datos de humedad y la segunda los de 
temperatura.

Cree un programa que determine, mediante una máscara, las posiciones de los elementos anomalos. Finalmente, 
llame a la función mostrar_anomalias() mandando como parámetros el array con las temperaturas y la máscara 
de los elementos anomalos. Analice los resultados del gráfico
'''

def mostrar_anomalias(datos, mascara):
    """
    muestra un grafico con datos de temperatura en funcion del tiempo y los puntos anomalos
    :param datos: numpy.array, datos de temperatura
    :param mascara: numpy.array, elementos anomalos
    """
    # se crea un indice que sera
    ind = np.arange(x.shape[0])

    # se muestra el grafico de la temperatura y los puntos anomalos
    fig, ax = plt.subplots(1, 1, figsize=(15, 5))
    ax.plot(ind, temp)
    ax.scatter(ind[mascara], datos[mascara], c="red", s=20)
    plt.show()
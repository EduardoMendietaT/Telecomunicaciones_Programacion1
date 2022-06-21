'''
Usando el mismo dataset que el ejercicio anterior, genere un gráfico donde se muestren en tres filas, 
la evolución de las siguientes variables: Temp, Rel_Hum, y Visibility. Estos valores deberán ser 
resampleados a una frecuencia de un mes, y se calcularán como sus datos promedio.

Las tres curvas deberán tener un color distinto, y deberán tener su respectiva leyenda.
'''

import pandas as pd
from matplotlib import pylab as plt


def mostrar_grafico_evolucion(df, xlabels, figsize, colors):
    '''Genera un plot con subplots de manera vertical que representan un grafica de linea de tiempo.
    PARAMS
    ------
    df : DataFrame
        Dataframe cuyas columnas queremos que apresca en la linea de tiempo.
    xlabels: str[]
        Nombre de las etiquetas que apreceran en el eje x, debe tener una cantidad de elementos igual al numero de columnas del dataframe.
    figsize : int ()
        Tupla con 2 valores enteros correspondientes al tamaño del plot en el eje x e y.
    colors : str []
        String con nombres de colores para cada linea de tiempo, debe tener una cantidad de elementos igual al numero de columnas del dataframe.
    '''
    columns = df.columns.tolist()
    fig, ax = plt.subplots(len(columns), 1, figsize = figsize, sharex = True)
    for i in range(len(columns)):
        df[columns[i]].plot(ax = ax[i], color = colors[i])
        ax[i].set_ylabel(xlabels[i])
    plt.show()


def main():
    df = pd.read_csv("./data/weather_2012.csv", sep=",", index_col=0, parse_dates=[0], encoding='utf-8-sig')
    dffilter = df.loc[ : , ['Temp', 'Rel_Hum', 'Visibility']].resample('M').mean()

    xlabels = ['Temperatura [°C]', 'Humedad Relativa [%]', 'Visibilidad [%]']
    colors = ['green', 'red', 'brown']
    mostrar_grafico_evolucion(dffilter, xlabels, (6, 5), colors)


if __name__ == '__main__':
    main()
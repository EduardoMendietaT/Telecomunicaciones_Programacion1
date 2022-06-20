'''
Usando el dataset weather_2012.csv genere un scatter plot para analizar la relación entre 
las variables Temp and Rel_Hum. Adicionalmente, se le pedirá al usuario que ingrese una fecha. 
El plot generado, mostrará los puntos que pertenecen al día ingresado de otro color.

Ayuda: para poder comparar una fecha ingresada con el índice, se debe crear un objeto de tipo 
datetime.date. Investigue como crear un objeto de este tipo y como usarlo para filtrar el dataset 
o generar una máscara.
'''

from cProfile import label
from datetime import datetime, date
from turtle import color
from matplotlib.pyplot import legend
import pandas as pd
from matplotlib import pylab as plt


def mostrar_grafico_scatter(x_dfs, figsize, xycols, xylabels, legends):
    colors = ['yellow', 'blue', 'green', 'red']
    fig, ax = plt.subplots(1, 1, figsize = figsize)
    
    for i in range(len(x_dfs)):
        x_dfs[i].plot(kind = 'scatter', ax = ax, x = xycols[0], y = xycols[1], c = colors[i], label = legends[i])
        ax.set_xlabel(xylabels[0])
        ax.set_ylabel(xylabels[1])
    ax.legend()
    plt.show()


def main():
    df = pd.read_csv("./data/weather_2012.csv", sep=",", index_col=0, parse_dates=[0], encoding='utf-8-sig')

    entrada = input('Ingrese una fecha con el siguiente formato: yyyy-MM-dd (Ejemplo 2022-05-13): ')
    fecha = datetime.strptime(entrada, '%Y-%m-%d').date()

    columns = ['Rel_Hum', 'Temp']
    dffilter = dffilter = df.loc[df.index.date == fecha, columns]

    xylabels = ('Humedad [%]', 'Temperatura [°C]')
    legends = ('Desde 2012-01-01 Hasta 2012-12-31', f'Fecha: {entrada}')
    mostrar_grafico_scatter([df, dffilter], (6, 5), columns, xylabels, legends)

    
    '''
    fig, ax = plt.subplots(1, 1, figsize = (6, 5))
    df.plot(kind = 'scatter', ax = ax, x = 'Rel_Hum', y = 'Temp', c = 'yellow')
    dffilter = df.loc[df.index.date == fecha, ['Temp', 'Rel_Hum']]
    dffilter.plot(kind = 'scatter', ax = ax, x = 'Rel_Hum', y = 'Temp', c = 'blue', label = f'Fecha: {entrada}')
    ax.set_xlabel('Humedad [%]')
    ax.set_ylabel('Temperatura [°C]')
    ax.legend()
    plt.show()'''


if __name__ == '__main__':
    main()
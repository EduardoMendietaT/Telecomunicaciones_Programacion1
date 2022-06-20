'''
Usando el dataset weather_2012.csv genere un scatter plot para analizar la relación entre 
las variables Temp and Rel_Hum. Adicionalmente, se le pedirá al usuario que ingrese una fecha. 
El plot generado, mostrará los puntos que pertenecen al día ingresado de otro color.

Ayuda: para poder comparar una fecha ingresada con el índice, se debe crear un objeto de tipo 
datetime.date. Investigue como crear un objeto de este tipo y como usarlo para filtrar el dataset 
o generar una máscara.
'''

from datetime import datetime, date
import pandas as pd
from matplotlib import pylab as plt


def main():
    df = pd.read_csv("./data/weather_2012.csv", sep=",", index_col=0, parse_dates=[0], encoding='utf-8-sig')

    entrada = input('Ingrese una fecha con el siguiente formato: yyyy-MM-dd (Ejemplo 2022-05-13): ')
    fecha = datetime.strptime(entrada, '%Y-%m-%d').date()

    dffilter = df.loc[df.index.date == fecha, ['Temp', 'Rel_Hum']]
    
    fig, ax = plt.subplots(1, 1, figsize = (6, 5))
    df.plot(kind = 'scatter', ax = ax, x = 'Rel_Hum', y = 'Temp', c = 'yellow', label = f'Desde 2012-01-01 hasta 2012-12-31')
    dffilter.plot(kind = 'scatter', ax = ax, x = 'Rel_Hum', y = 'Temp', c = 'blue', label = f'Fecha: {entrada}')
    ax.set_xlabel('Humedad [%]')
    ax.set_ylabel('Temperatura [°C]')
    ax.legend()
    plt.show()


if __name__ == '__main__':
    main()
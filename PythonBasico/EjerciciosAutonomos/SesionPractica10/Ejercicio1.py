'''
Genere un programa que dado una región, muestre un gráfico de barras con los valores de Happiness Score 
de los países pertenecientes a esa región. Para ello, usar el dataset felicidad-2016.csv.

El gráfico seleccionado deberá tener un tamaño lo suficientemente grande para poderlo visualizar claramente. 
Además, deberá tener las etiquetas en los ejes x y y
'''

import pandas as pd
from matplotlib import pylab as plt


def filtrar_por_columna(df, columfilter, valuefilter, colums_get):
    regiones = df.loc[df[columfilter] == valuefilter, colums_get]
    return regiones

    
def mostrar_plot_barras(xdf, ydf, size):
    plt.figure(figsize = size)
    plt.barh(ydf, xdf, color = 'blue')
    plt.xlabel('Happiness Score')
    plt.ylabel('Paises')
    plt.show() 


def main():
    df = pd.read_csv('./data/felicidad-2016.csv')
    region = input('\nIngrese una región: ')
    regiones = filtrar_por_columna(df, 'Region', region, ['Country', 'Happiness Score'])
    mostrar_plot_barras(regiones['Happiness Score'], regiones['Country'], (6, 1.5))
    

if __name__ == '__main__':
    main()
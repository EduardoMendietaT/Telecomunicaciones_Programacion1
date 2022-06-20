'''
Usando el mismo dataset que en el Ejercicio 1, genere un programa que muestre una figura 
con tres subplots (uno encima de otro), donde la información de los países a usarse estará 
seleccionada por su región (similar al ejercicio 1). El primer plot mostrará el GDP per capita; 
el segundo plot mostrará los valores de la columna Family; y, el tercer plot los valores de la 
columna Freedom. Todos los plots mostrarán gráficos de barras, y sus valores estarán ordenados 
de mayor a menor.
'''
import pandas as pd
from matplotlib import pylab as plt


filtrardf = lambda df, cfilter, vfilter, cols: df.loc[df[cfilter] == vfilter, cols]


def mostrar_grafico_barras(xdf, figsize, ascending):
    colours = ['orange','green', 'blue', 'yellow', 'red']
    columnnames = xdf.columns.tolist()
    numsubplots = len(columnnames)
    fig, ax = plt.subplots(numsubplots, 1, figsize = figsize)
    for i in range(numsubplots):
        axval = ax[i] if numsubplots != 1 else ax
        xdf[columnnames[i]].sort_values(ascending = ascending).plot(kind = 'barh', ax = axval, color = colours[i])
        axval.set_xlabel(columnnames[i])
    fig.tight_layout()
    plt.show()


def main():
    df = pd.read_csv('./data/felicidad-2016.csv', index_col = 0, sep=",", encoding='utf-8-sig')
    region = input('\nIngrese una región: ')

    cfilter = 'Region'
    columns = ['Economy (GDP per Capita)', 'Family', 'Freedom']

    dffilter = filtrardf(df, cfilter, region,  columns)
    mostrar_grafico_barras(dffilter, (6, 6), False)


if __name__ == '__main__':
    main()
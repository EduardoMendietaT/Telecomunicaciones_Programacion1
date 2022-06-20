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


def filtrar_por_columna(df, columfilter, valuefilter, colums_get):
    regiones = df.loc[df[columfilter] == valuefilter, colums_get]
    return regiones


def mostrar_subplots_barras(dfs_x, df_y, xylabels, figuresize, ejes, colorsplots):
    fig, ax = plt.subplots(ejes[0], ejes[1], figsize = figuresize, sharex = True)
    for i in range(len(dfs_x)):
        ax[i].barh(df_y, dfs_x[i], color = colorsplots[i])
        ax[i].set_xlabel(xylabels[i][0])
        ax[i].set_ylabel(xylabels[i][1])
    plt.show()


def main():
    df = pd.read_csv('./data/felicidad-2016.csv')
    region = input('\nIngrese una región: ')
    columns = ['Country', 'Economy (GDP per Capita)', 'Family', 'Freedom']
    regiones = filtrar_por_columna(df, 'Region', region, columns)

    dfs_x = [regiones[columns[i]] for i in range(1, len(columns))]
    df_y = regiones[columns[0]]
    xylabels = [(columns[i], columns[0]) for i in range(1, len(columns))]
    figuresize = (6, 6)
    ejes = (3, 1)
    colorsplots = ['orange', 'green', 'blue']
 
    mostrar_subplots_barras(dfs_x, df_y, xylabels, figuresize, ejes, colorsplots)


if __name__ == '__main__':
    main()
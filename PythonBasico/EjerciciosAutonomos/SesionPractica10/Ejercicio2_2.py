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
ordenardf = lambda df, by, ascending: df.sort_values(by, ascending = ascending)   

def main():
    df = pd.read_csv('./data/felicidad-2016.csv', index_col = 0, sep=",", encoding='utf-8-sig')
    region = input('\nIngrese una región: ')
    cfilter = 'Region'
    colsnames = ['Economy (GDP per Capita)', 'Family', 'Freedom']

    economydf = ordenardf(filtrardf(df, cfilter, region, [colsnames[0]]), colsnames[0], False)
    familydf = ordenardf(filtrardf(df, cfilter, region, [colsnames[1]]), colsnames[1], False)
    freedomdf = ordenardf(filtrardf(df, cfilter, region, [colsnames[2]]), colsnames[2], False)

    res = pd.DataFrame([economydf, familydf, ])
    print(freedomdf.head())
    

    '''fig, ax = plt.subplots(1, 1, figsize = (6, 6))
    df.loc[df['Region'] == region, ['Happiness Score']].plot(kind = 'barh', ax = ax)
    ax.set_xlabel('Score de Felicidad')
    plt.show()'''


if __name__ == '__main__':
    main()
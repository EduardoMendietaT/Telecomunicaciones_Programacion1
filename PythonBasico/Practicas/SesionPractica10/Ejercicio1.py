'''
Genere un programa que dado una región, muestre un gráfico de barras con los valores de Happiness Score 
de los países pertenecientes a esa región. Para ello, usar el dataset felicidad-2016.csv.

El gráfico seleccionado deberá tener un tamaño lo suficientemente grande para poderlo visualizar claramente. 
Además, deberá tener las etiquetas en los ejes x y y
'''

import pandas as pd
from matplotlib import pylab as plt


# Filtra un dataframe(df: DatFrame) recibido por parametros utilizando los valores de una column(cfilter: str)
# y comparandolos con un valor(vfilter: str), ademas extrae las columnas que se pasan por parametro(cols: str[])
filtrardf = lambda df, cfilter, vfilter, cols: df.loc[df[cfilter] == vfilter, cols]


def mostrar_grafico_barras(xdf, figsize, ascending):
   '''Genera un plot con varios subplots en forma vertical para graficos de barras.
   PARAMS
   ------
   xdf : DataFrame
      DataFrame cuya columnas deseamos que se muestren en el grafico de barras.
   
   figsize : int ()
      Tupla con 2 valores enteros correspondientes al tamaño del plot en el eje x e y.
   
   ascending : bool
      True si se desea ordenar las columnas del DataFrame de forma ascendente.
   '''
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
   df = pd.read_csv('./data/felicidad-2016.csv', index_col = 0, sep = ",", encoding = 'utf-8-sig')

   region = input('\nIngrese una región: ')

   cfilter = 'Region'
   columns = ['Happiness Score']
   dffilter = filtrardf(df, cfilter, region, columns)
   mostrar_grafico_barras(dffilter, (6, 6), True)
   
    
if __name__ == '__main__':
    main()
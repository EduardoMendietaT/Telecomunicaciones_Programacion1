'''
El índice global de felicidad es una publicación anual de las Naciones Unidas que mide la felicidad en 157 países, basándose en diversos factores, 
como el PIB per cápita. Se requiere conocer la situación de Ecuador con respecto al resto de países del mundo. Para ello:

Leer en un DataFrame los datos del archivo felicidad-2016.csv
una vez haya leído el archivo, muestre las columnas del DataFrame y los primeros 10 registros (para ello use la función .head())
Muestre cuál es Happiness Score de Ecuador y el score promedio del resto de los países. Ecuador está por sobre la media o por debajo?
P.D. como ayuda, use el campo Country como índice del DataFrame
'''

import pandas as pd

df = pd.read_csv('felicidad-2016.csv', index_col = 0, sep = ',', encoding = 'utf-8-sig')
df.head(10)

prom_felecidad_mundial = df[df.index != 'Ecuador']['Happiness Score'].mean()
indice_felicidad_ecuador = df.loc['Ecuador', 'Happiness Score']

print(f'\nPromedio de felicidad mundial: {prom_felecidad_mundial} vs indice de felicidad en Ecuador: {indice_felicidad_ecuador}\n')

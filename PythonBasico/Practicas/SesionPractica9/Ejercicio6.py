'''
En el DataFrame anterior, existe una columna denominada Weather con múltiples valores. Una empresa está interesada en la relación 
entre visibilidad y clima cuando hay neblina (Fog). Calcule, en términos porcentuales cuanta visibilidad se pierde en días en los 
que hay neblina. Adicionalmente, cuál es el porcentaje de días en donde se tiene neblina.

Ayuda:

Investigue como buscar un substring en una columna. Busque los elementos que tengan Fog en la columna Visibility
'''
import pandas as pd 
import numpy as np

df = pd.read_csv('weather_2012.csv', index_col = 0, sep = ',', encoding = 'utf-8-sig', parse_dates = [0])

total_dias = np.unique(df.index.date).size

datos_fog = df['Weather'].str.contains('Fog')

num_dias_fog = np.unique(df.loc[datos_fog].index.date).size

porcentaje_dias_fog = round(num_dias_fog * 100 / total_dias, 2)

prom_dias_fog = df.loc[datos_fog]['Visibility'].mean()
prom_dias_nofog = df.loc[~datos_fog]['Visibility'].mean()

porcentaje_visibilidad_perdido = 100 - round(prom_dias_fog * 100 /prom_dias_nofog, 2)

print(f'\nSe pierde un {porcentaje_visibilidad_perdido}% de visibilidad en días con neblina.')
print(f'El porcentaje de días en los que se tiene niebla es del {porcentaje_dias_fog}%.\n')
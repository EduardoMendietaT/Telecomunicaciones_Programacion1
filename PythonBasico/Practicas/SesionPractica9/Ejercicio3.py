'''
Generar un reporte donde se muestren los Happiness Score promedios por Región. Dichos valores deberán estar ordenados de menor a mayor.
'''
import pandas as pd

df = pd.read_csv('felicidad-2016.csv', index_col = 0, sep = ',', encoding = 'utf-8-sig')

promedio_felicidad_region = df.loc[:, ['Region', 'Happiness Score']].groupby('Region').mean().sort_values(by = 'Happiness Score')

print(f'\n{promedio_felicidad_region}\n')
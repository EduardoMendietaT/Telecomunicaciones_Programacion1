'''
Se requiere hacer una comparación del coportamiento del consumo energético por año (2002 - 2018). Se mostrará en forma de un tabla los valores medios de consumo, 
valores máximos y mínimos. La ciudad espera que durante este lapso de tiempo, el consumo energético decreció debido a las múltiples medidas tomadas. 
¿Se puede decir que el consumo energético promedio ha decrecido en estos años?

Ayuda: puede usar la función agg()
'''
import pandas as pd

df = pd.read_csv("PJME_hourly.csv", index_col=0, parse_dates=[0], encoding = 'utf-8-sig')

df['promedio'] = df['PJME_MW']
df['valor_maximo'] = df['PJME_MW']
df['valor_minimo'] = df['PJME_MW']

res = df.groupby(df.index.year).agg({'promedio': 'mean', 'valor_maximo': 'max', 'valor_minimo':'min'})

print(f'\n{res}\n')
'''
Usando como base el ejercicio anterior, ¿Cuales son los 3 primeros países en términos de Happiness Score?; y, 
¿Cuáles son los 3 países con menor Score?. Muestre en una tabla: El País, el Score, el Health (Life Expectancy), 
y la Region
'''
import pandas as pd

df = pd.read_csv('felicidad-2016.csv', index_col = 0, sep = ',', encoding = 'utf-8-sig')
df.head(10)

def get_registros(df, n, isascending):
    res = df.loc[: ,['Happiness Score', 'Health (Life Expectancy)', 'Region']].sort_values(by = 'Happiness Score', ascending = isascending).head(n)
    return res

max_score = get_registros(df, 3, False)
min_score = get_registros(df, 3, True)

maxmin_score_felicidad = pd.concat([max_score, min_score])

print(get_registros(maxmin_score_felicidad, maxmin_score_felicidad.size, False))

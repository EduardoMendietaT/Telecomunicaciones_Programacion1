'''
Se requiere mostrar la información del dataset felicidad-2016.csv, pero únicamente de ciertos países. Para ello, realizar lo siguiente:

Pedir un listado de países al usuario (ingresar paises separados por comas)
Verificar si los países existen en el DataFrame. Si algún país no existe, descartarlo
Mostrar toda la información disponible de los países ingresados
'''
import pandas as pd

df = pd.read_csv('felicidad-2016.csv', index_col = 0, sep = ',', encoding = 'utf-8-sig')

def get_registros(df, n, isascending):
    res = df.loc[: ,['Happiness Score', 'Health (Life Expectancy)', 'Region']].sort_values(by = 'Happiness Score', ascending = isascending).head(n)
    return res

entrada = input('\nIngrese nombres de paises separados por comas(ejm: Ecuador,Bolivia,Colombia): ')

paises = [i for i in entrada.split(',') if i in df.index]

resultado = df.loc[paises, :]

print(f'\n{resultado.head(resultado.size)}\n')
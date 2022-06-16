'''
Usando el DataFrame anterior, se requiere categorizar las temperaturas encontradas. Para ello, se definen las siguientes categorías para la temperatura ():

Categoria 1: 
Categoria 2: 
Categoria 3: 
Categoría 4: 
'''
import pandas as pd

dsw = pd.read_csv('weather_2012.csv', index_col = 0, sep = ',', encoding = 'utf-8-sig', parse_dates = [0]) 

def generar_nueva_columna(Temp):
    if Temp <= 0:
        return 'Categoria 1'
    elif 0 < Temp <= 10:
        return 'Categoria 2'
    elif 10 < Temp <= 20:
        return 'Categoria 3'
    elif Temp > 20:
        return 'Categoria 4'
    

dsw['Categoria'] = dsw['Temp'].apply(generar_nueva_columna)
print(dsw.head(dsw.size))
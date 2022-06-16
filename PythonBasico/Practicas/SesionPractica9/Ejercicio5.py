'''
La función np.unique() del paquete numpy retorna los elementos únicos de una lista o array. Esta funcionalidad es muy útil en casos en donde 
se requiera saber que valores puede tener una variable. Adicionalmente, cuando se manejan elementos de tipo Date en pandas, muchas veces se 
tienen frecuencias menores a un día (varias mediciones por día). Para conocer cuantos días existen en un dataset, se puede ejecutar el siguiente 
comando:

np.unique(ds.index.date).size

considerando que ds es un DataFrame que tiene un índice de tipo Date (como en el ejercicio anterior)

El archivo weather_2012.csv contiene información ambiental en un lugar específico. Entre otras cosas tiene la temperatura (Temp), 
humedad relativa (Rel_Hum), velocidad del viento (Wind_Spd), visibilidad (Visibility), tipo de clima (Weather).

Una compañia dedicada a la salud y cuidado del hogar está realizando un estudio de la situación actual de la región de estudio. 
Esta compañia busca determinar cuan problemático podría llegar a ser la humedad relativa en la salud de las personas. Para ello, 
determina que necesita conocer cuantos días existieron en donde la humedad relativa estuvo fuera del rango de 15% -75%. Implemente 
esta funcionalidad y muestre la cantidad de días en donde existieron valores de humedad relativa fuera de este rango y muestre el 
número total de días que existen en el DataFrame. Finalmente, calcule el porcentaje de días que estuvieron fuera del rango antes descrito.
'''
import pandas as pd 
import numpy as np

df = pd.read_csv('weather_2012.csv', index_col = 0, sep = ',', encoding = 'utf-8-sig', parse_dates = [0])

total_dias = np.unique(df.index.date).size

res = df.loc[(df['Rel_Hum'] < 15) | (df['Rel_Hum'] > 75)]


num_dias_fuera_rango = np.unique(res.index.date).size

porcentaje = num_dias_fuera_rango * 100 / total_dias

print(f'\nNúmero de días fuera del rango 15% - 75%: {num_dias_fuera_rango}\nNúmero total de días: {total_dias}')
print(f'Porcentaje de dias que estubieron fuera del rango: {round(porcentaje, 2)}%\n')
'''
El archivo PJME_hourly.csv contiene información sobre el consumo energético en megawats en una ciudad. Se requiere conocer el comportamiento 
del consumo energético durante los días de trabajo (lunes a viernes) y los fines de semana. Compare el consumo promedio entre estas dos categorías. 
La hipótesis que maneja la ciudad es que el consumo el fin de semana se reduce sustancialmente.

Ejecute el código a continuación para visualizar el comportamiento del consumo energético en función del tiempo

fig, ax = plt.subplots(1, 1, figsize=(18, 3))

ds = pd.read_csv("PJME_hourly.csv", index_col=0, parse_dates=[0])
ds.plot(ax=ax)
'''
import pandas as pd;
import numpy as np

df = pd.read_csv("PJME_hourly.csv", index_col=0, parse_dates=[0], encoding = 'utf-8-sig')

df_consumos_lunvie = df.loc[(df.index.dayofweek != 5) & (df.index.dayofweek != 6)]
df_consumos_finsemana = df.loc[(df.index.dayofweek == 5) | (df.index.dayofweek == 6)]

prom_consumo_lunVie = round(df_consumos_lunvie['PJME_MW'].mean(), 2)
prom_consumo_finsemana = round(df_consumos_finsemana['PJME_MW'].mean(), 2)

print(f'\nEl consumo promedio de Lun - Vie es: {prom_consumo_lunVie} y el consumo promedio de los fines de semana es: {prom_consumo_finsemana}\n')
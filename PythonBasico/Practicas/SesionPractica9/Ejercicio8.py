'''
El archivo power_consumption.csv contiene mediciones de consumo de potencia en una casa. Estas mediciones tiene una frecuencia de 1 minuto y sus columnas se 
describen a continuación:

DateTime: Index information
global_active_power: The total active power consumed by the household (kilowatts).
global_reactive_power: The total reactive power consumed by the household (kilowatts).
voltage: Average voltage (volts).
global_intensity: Average current intensity (amps).
sub_metering_1: Active energy for kitchen (watt-hours of active energy).
sub_metering_2: Active energy for laundry (watt-hours of active energy).
sub_metering_3: Active energy for climate control systems (watt-hours of active energy).
Se requiere analizar los valores máximos de consumo del hogar en lapsos de tiempo de 15 minutos, en vez de 1 minuto. Entonces, el DataFrame deberá ser 
re-sampleado a una frecuencia de 15 minutos. Adicionalmente, se requieren encontrar los outliers (valores anómalos) en términos de potencia activa y reactiva. 
Para ello, un valor de potencia activa se considera anómalo si sobrepasa los 4 kwh. Así mismo, un valor de potencia reactiva se considera anómalo si sobrepasa los 0.5 kwh.

Genere tres DataFrames: (1) con la información original re-sampleada a 15 minutos, tomando en cuenta los valores máximos; (2) con los outliers de potencia 
activa; y, (3) con los outliers de potencia reactiva.

Ejecute la función mostrar_potencia(d, dogap, dogrp) mandando como parámetros, los tres dataframes formados anteriormente.

Finalmente, mostrar las fechas en las que estos outliers sucedieron.
'''
import pandas as pd
import matplotlib.pylab as plt
import numpy as np


def mostrar_potencia(d, dogap, dogrp):
    fig, ax = plt.subplots(2, 1, figsize=(18, 3), sharex=True)
    d["Global_active_power"].plot(ax=ax[0])
    d["Global_reactive_power"].plot(ax=ax[1])
    dogap["Global_active_power"].plot(ax=ax[0], style="o")
    dogrp["Global_reactive_power"].plot(ax=ax[1], style="o")


df = pd.read_csv('power_consumption.csv', index_col = 0, sep = ',', encoding = 'utf-8-sig', parse_dates = [0])
df_resmp = df.resample('15min').max()

df_pa_outliers = df_resmp.loc[df_resmp['Global_active_power'] >	4]

df_pr_outliers = df_resmp.loc[df_resmp['Global_reactive_power'] > 0.5]

mostrar_potencia(df_resmp, df_pa_outliers, df_pr_outliers)

fechas_outliers = np.concatenate([np.unique(df_pa_outliers.index.date), np.unique(df_pr_outliers.index.date)])

print(f'\nFechas de los outliers: {[i.strftime("%d/%m/%Y") for i in fechas_outliers]}\n')
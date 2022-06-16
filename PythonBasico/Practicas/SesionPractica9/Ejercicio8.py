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

df = pd.read_csv('power_consumption.csv', index_col = 0, sep = ',', encoding = 'utf-8-sig', parse_dates = [0])
print(df.head())
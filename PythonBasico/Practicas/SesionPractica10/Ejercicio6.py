'''
Basándose en el ejercicio 10 de la sesión de ejercicios anterior, genere una figura con las 3 curvas 
correspondientes al valor promedio, mínimo, y máximo de potencia. Cada curva deberá estar en el mismo 
plot, deberá tener un color distinto, y deberá tener una leyenda descriptiva.
'''
from cProfile import label
import pandas as pd
from matplotlib import pylab as plt

def main():
    df = pd.read_csv("./data/PJME_hourly.csv", index_col=0, parse_dates=[0], encoding = 'utf-8-sig')
    
    df['promedio'] = df['PJME_MW']
    df['valor_maximo'] = df['PJME_MW']
    df['valor_minimo'] = df['PJME_MW']

    res = df.groupby(df.index.year).agg({'promedio': 'mean', 'valor_maximo': 'max', 'valor_minimo':'min'})

    print(f'\n{res}\n')

    fig, ax = plt.subplots(1, 1, figsize = (5, 5))
    res['promedio'].plot(ax = ax, color = 'red', label = 'Promedio')
    res['valor_maximo'].plot(ax = ax, color = 'blue', label = 'Máximo')
    res['valor_minimo'].plot(ax = ax, color = 'green', label = 'Mínimo')
    ax.legend()
    ax.set_xlabel('Tiempo [Años]')
    ax.set_ylabel('Potencia [MW]')
    plt.show()

if __name__ == '__main__':
    main()
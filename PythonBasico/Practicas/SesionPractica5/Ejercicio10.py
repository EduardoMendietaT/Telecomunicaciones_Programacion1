'''
Este ejercicio tiene por objeto que el alumno trabaje con datos reales y obtenga información de relevancia. 
Para ello, se define una función leer_datos() que lee datos de un archivo conteniendo información sobre la 
tasa de crimen y robos por cada 100000 habitantes en USA. Esta función retorna 3 listas: year (año), 
vcr (violent crime rate), y rr (robbery rate). El estudiante no debe modificar nada de esta función, simplemente 
usar ejecutar el código para obtener las 3 listas antes descritas.
'''
import pandas as pd

def leer_datos(imprimir=False):
    """Función para leer los datos del dataset crime_usa
    
    Returns
    year: list, lista conteniendo los años en los que se realizaron mediciones
    vcr: list, violent crime rate de cada año descrito en year
    rr: list, robbery rate de cada año descrito en year
    """
    ds = pd.read_csv("crime_usa.csv", header=0, index_col=0, sep=',')
    
    if imprimir:
        print(ds)  # muestra la estructura del dataset
    
    return list(ds.index), list(ds.violent_crime_rate), list(ds.robbery_rate)

year, vcr, rr = leer_datos(imprimir=True)

'''
Cree código para obtener la siguiente información:
Año en el que la tasa de crímenes violentos fue la menor. También mostrar el valor de la tasa
Año en el que la tasa de robos fue la menor. También mostrar el valor de la tasa
Año en el que la tasa de crímenes violentos fue la mayor. También mostrar el valor de la tasa
Año en el que la tasa de robos fue la mayor. También mostrar el valor de la tasa
'''

# Ordenamo la lista de crimenes y robos, extraemos el mayor y menor valor de cada uno.
t_min_crimen = sorted(vcr)[0]
t_max_crimen = sorted(vcr)[-1]
t_min_robo = sorted(rr)[0]
t_max_robo = sorted(rr)[-1]

# Ubicamos el indice de la tasa mayor y menor, para encontrar sus repectivos años.
for index, value in enumerate(vcr):
    if t_max_crimen == value:
        a_max_crimen = year[index] 
    if t_min_crimen == value:
        a_min_crimen = year[index]

# Ubicamos el indice de la tasa mayor y menor, para encontrar sus repectivos años.
for index, value in enumerate(rr):
    if t_max_robo == value:
        a_max_robo = year[index] 
    if t_min_robo == value:
        a_min_robo= year[index]

# Imprimos los años con sus tasas por consola.
print(f'\nEl año en el que la tasa de crimen fue manor es {a_min_crimen}, con una tasa de crimenes de {t_min_crimen}.')
print(f'El año en el que la tasa de crimen fue mayor es {a_max_crimen}, con una tasa de crimenes de {t_max_crimen}.')
print(f'El año en el que la tasa de robo fue menor es {a_min_robo}, con una tasa de robos de {t_min_robo}.')
print(f'El año en el que la tasa de robo fue mayor es {a_max_robo}, con una tasa de robos de {t_max_robo}.\n')


'''
Haciendo uso de un diccionario, cree una estructura en donde se tengan 3 categorías de crímenes violentos: (1) baja (0-400), 
(2) media (400-500); y, (3) alta (>500). Por cada categoría, almacenar el promedio de la tasa de críemenes violentos y los 
años que se encasillan en esta categoría.

Al final mostrar el diccionario creado.

Salida esperada: {'baja': {'anios': [2011, 2012, 2013, 2014, 20156, 2016], 'promedio': 5037.0}, 'media': {'anios': [2002, 
2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], 'promedio': 2006.0}, 'alta': {'anios': [1997, 1998, 1999, 2000, 20015], 
'promedio': 5601.8}}
'''
# Creamos un diccionario con categorias predefinidas:
categorias = {
    'baja': {'años': [], 'promedio': 0, 'numElementos': 0}, 
    'media': {'años': [], 'promedio': 0, 'numElementos': 0}, 
    'alta': {'años': [], 'promedio': 0, 'numElementos': 0}}

# Seteamos los valores por defecto de las categorias con los años y suma de elementos de crimenes.
for index, value in enumerate(vcr):
    if 0 < value <= 400:
        categorias['baja']['años'] += [year[index]]
        categorias['baja']['promedio'] += value
        categorias['baja']['numElementos'] += 1
    elif 400 < value <= 500:
        categorias['media']['años'] += [year[index]]
        categorias['media']['promedio'] += value
        categorias['media']['numElementos'] += 1
    else:
        categorias['alta']['años'] += [year[index]]
        categorias['alta']['promedio'] += value
        categorias['alta']['numElementos'] += 1

# Calculamos el promedio de los crimenes de cada categoria.
for i in categorias.values():
    elementos = i['numElementos']
    i['promedio'] = round(i['promedio']/elementos, 2)
    i.pop('numElementos')

print(f'\nSalida: {categorias}\n')
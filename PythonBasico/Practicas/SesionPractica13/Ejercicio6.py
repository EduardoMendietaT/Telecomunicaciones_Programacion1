'''
Este ejercicio tiene por objetivo que el estudiante practique en sus habilidades de diseño de programas.
Para un correcto diseño de programas se deben seguir los siugientes lineamientos:

1) Especificar el conjunto de funciones a usar. Por cada función se debe establecer:

El nombre de la función
El docstring de cada función (entradas, salidas, tipos de datos, descripción)
2) Bosquejar la implementación de la función. Se puede usar lenguaje natural para describir que se va a implementar

La funcionalidad a implementar es la siguiente: Se requiere un programa que lea un archivo de texto (texto.txt) y 
muestre los siguientes resultados:

El número de palabras en el archivo
Las 10 palabras más frecuentes en el texto
El número de veces que se repite una palabra
El programa pedirá al usuario que ingrese el nombre del archivo y la palabra a buscar. Adicionalmente, el programa 
deberá tener todas las características de programación defensiva (correcto uso de try ... except y asserts)

Nota: debe tener en cuenta todas las posibles fallas que podría haber en el programa, e.j. el archivo no existe, 
se ingresó una palabra vacía, se ingresó un número negativo para palabras frecuentes, etc. De encontrarse un error, 
el programa deberá parar su ejecución mostrando un mensaje entendible para el usuario.
'''
from io import open
import pandas as pd

def leerarchivo(ruta):
    archivotxt = open(ruta, 'r')
    texto = archivotxt.read()
    archivotxt.close()
    return texto


def get_palabras(texto):
    char_espc = ['.', '-', ',', ':', ';', '\n']
    for i in char_espc:
        texto = texto.replace(i, ' ')
    palabras = [i.lower().strip() for i in texto.split(' ') if len(i.strip()) > 0]
    num_elementos = len(palabras)
    df = pd.DataFrame(palabras, columns = ['palabras'])
    return df, num_elementos


def filtrar_por_numocurrencias(palabras_df, ascending):
    df = palabras_df.groupby('palabras').size().reset_index(name = 'num_ocurrencias')
    df = df.sort_values('num_ocurrencias', ascending = ascending)
    return df


def get_mas_frecuentes(palabras_df, num_palabras):
    df = filtrar_por_numocurrencias(palabras_df, False)
    masfrecuentes = df.head(num_palabras)['palabras'].tolist()
    return masfrecuentes


def get_num_ocurrencias(palabras_df, palabra):
    df = filtrar_por_numocurrencias(palabras_df, False)
    ocurrencias = 0
    aux = df.loc[df['palabras'] == palabra, ['num_ocurrencias']]
    if aux.size > 0:
        ocurrencias = int(aux.iloc[0])
    return ocurrencias


def main():
    nombre_archivo = input('\nIngrese el nombre del archivo(Ejm -> texto.txt): ')
    palabra = input('Ingrese una palabra para buscar en el archivo: ')
    texto = leerarchivo(f'./data/{nombre_archivo}')
    palabras_df, num_palabras = get_palabras(texto)
    print(f'\nNúmero de palabras del archivo: {num_palabras}.')
    print(f'Las 10 palabras mas frecuentes en el texto: {get_mas_frecuentes(palabras_df, 10)}.')
    print(f'Número de veces que se repite la palabra "{palabra}" en el texto: {get_num_ocurrencias(palabras_df, palabra)}.\n')


if __name__ == '__main__':
    main()
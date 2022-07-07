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
import logging


def leerarchivo(ruta):
    '''lee un archivo externo.
    PARAMS
    ______
    ruta : str
        ruta en la que se encuentra ubicado el archivo.
    RETURN
    ______
    texto : str
        texto contenido en el archivo externo.
    '''
    assert type(ruta) == str, 'La ruta del archivo tiene que ser un string!'
    assert ruta.count('.txt') == 1, 'Debe agragar la extensión .txt después del nombre del archivo!'

    archivotxt = open(ruta, 'r')
    texto = archivotxt.read()
    archivotxt.close()
    return texto


def get_palabras(texto):
    '''Transforma un texto en un DataFrame con todas las palabras encontradas en dicho texto.
    PARAMS
    ______
    texto : str
        texto del cual se extraeran todas las palabras.
    RETURN
    ______
    df : DataFrame
        DataFrame que contiene un columna con todas las palabras del "texto" pasado compo parametro.
    num_elementos : int
        Número de palabras encontradas en el texto.
    '''
    assert type(texto) == str, 'El texto debe ser de tipo string!'
    assert len(texto) > 0, 'No se puede enviar un texto vacío!'

    # reamos una lista con caracteres especiales.
    char_espc = ['.', '-', ',', ':', ';', '\n']
    # Eliminamos todos los caracteres especiales del texto.
    for i in char_espc:
        texto = texto.replace(i, ' ')
    palabras = [i.lower().strip() for i in texto.split(' ') if len(i.strip()) > 0]
    num_elementos = len(palabras)
    df = pd.DataFrame(palabras, columns = ['palabras'])
    return df, num_elementos


def filtrar_por_numocurrencias(palabras_df, ascending):
    '''Crea un DataFrame sin repetir las palabras y añidiendo una nueva columna con el número de ocurrencias de cada una.
    PARAMS
    ______
    palabras_df : DataFrame
        DataFrame que contiene la lista de palabras con un nombre de column igual a 'palabras'.
    ascending : bool
        si es True ordenara el DataFrame de manera ascendente por el campo de 'num_ocurrencias' caso contrario lo ordenara de manera descendente.
    RETURN
    ______
    df : DataFrame
        DataFrame filtrado con la nueva columna de ocurrencias.
    '''
    assert type(palabras_df) == pd.core.frame.DataFrame, 'El parametro "palabras_df" debe ser un objeto DataFrame de Pandas!'
    assert type(ascending) == bool, 'El parametro "ascending" debe ser de tipo bool!'
    assert palabras_df.shape[1] == 1, 'El DataFrame "palabras_df" debe contener una unica fila con palabras!'
    assert 'palabras' in palabras_df.columns.tolist(), 'El DataFrame "palabras_df" debe contener una columna con el nombre "palabras"!'

    df = palabras_df.groupby('palabras').size().reset_index(name = 'num_ocurrencias')
    df = df.sort_values('num_ocurrencias', ascending = ascending)
    return df


def get_mas_frecuentes(palabras_df, num_palabras):
    '''Crea una lista con el número de palabras 'num_palabras' mas frecuentes en el DataFrame 'palabras_df'
    PARAMS
    ______
    palabras_df : DataFrame
        DataFrame que contiene la lista de palabras con un nombre de column igual a 'palabras'.
    num_palabras : int
        Número de palabras mas frecuentes que se desea encontrar.
    RETURN
    ______
    masfrecuentes : list<str>
        lista con las palabras mas frecuentes.
    '''
    assert type(palabras_df) == pd.core.frame.DataFrame, 'El parametro "palabras_df" debe ser un objeto DataFrame de Pandas!'
    assert type(num_palabras) == int, 'El parametro "num_palabras" debe ser de tipo entero!'
    assert num_palabras > 0, 'El parametro "num_palabras" debe ser mayor a cero!'
    assert palabras_df.shape[1] == 1, 'El DataFrame "palabras_df" debe contener una unica fila con palabras!'
    assert 'palabras' in palabras_df.columns.tolist(), 'El DataFrame "palabras_df" debe contener una columna con el nombre "palabras"!'

    df = filtrar_por_numocurrencias(palabras_df, False)
    masfrecuentes = df.head(num_palabras)['palabras'].tolist()
    return masfrecuentes


def get_num_ocurrencias(palabras_df, palabra):
    '''Busca el núemro de ocurrencias de la palabra 'palabra' en el DataFrame 'palabras_df'
    PARAMS
    ______
    palabras_df : DataFrame
        DataFrame que contiene la lista de palabras con un nombre de column igual a 'palabras'.
    palabra : str
        Palabra que se desea buscar su número de ocurrencias.
    RETURN
    ______
    ocurrencias : int
        Número de veces que se repite la palabra en el DataFrame 'palabras_df'
    '''
    assert type(palabras_df) == pd.core.frame.DataFrame, 'El parametro "palabras_df" debe ser un objeto DataFrame de Pandas!'
    assert type(palabra) == str and len(palabra) > 0, 'El parametro "palabra" debe ser de tipo String y no debe estar vacio!'
    assert palabras_df.shape[1] == 1, 'El DataFrame "palabras_df" debe contener una unica fila con palabras!'
    assert 'palabras' in palabras_df.columns.tolist(), 'El DataFrame "palabras_df" debe contener una columna con el nombre "palabras"!'

    # Obtenemos un DataFrame con el número de ocurrencias por palabra.
    df = filtrar_por_numocurrencias(palabras_df, False)
    ocurrencias = 0
    # Buscamos la palabra dentro del DataFrame.
    aux = df.loc[df['palabras'] == palabra, ['num_ocurrencias']]
    if aux.size > 0:
        ocurrencias = int(aux.iloc[0])
    return ocurrencias


def main():
    # Creamos un objeto logger para capturar los posibles mensajes de error.
    logger = logging.getLogger()

    # Pedimos los datos al usuario.
    nombre_archivo = input('\nIngrese el nombre del archivo(Ejm -> texto.txt): ')
    palabra = input('Ingrese una palabra para buscar en el archivo: ')
    
    # Leemos el archivo y capturamos los posibles errores.
    try:
        texto = leerarchivo(f'./data/{nombre_archivo}')
        palabras_df, num_palabras = get_palabras(texto)
        print(f'\nNúmero de palabras del archivo: {num_palabras}.')
        print(f'Las 10 palabras mas frecuentes en el texto: {get_mas_frecuentes(palabras_df, 10)}.')
        print(f'Número de veces que se repite la palabra "{palabra}" en el texto: {get_num_ocurrencias(palabras_df, palabra)}.\n')
    except FileNotFoundError:
        print(f'\nNo se puede encontrar el archivo con el nombre: "{nombre_archivo}".\n')
    except AssertionError as e:
        logger.error(f'\n{str(e)}\n')
    except ValueError:
        print(f'\nOcurrio un error al intentar transformar a entero en la función: "filtrar_por_numocurrencias".\n')


if __name__ == '__main__':
    main()
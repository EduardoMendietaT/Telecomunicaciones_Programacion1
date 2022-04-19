# 19. ARCHIVOS: ----------------------------------------------------------------------------------------
# open(nombre_archivo, modo) --> Modos: 'r' - lectura, 'w' - escritura, 'a' - agregar, 'r+' - lectura y escritura, 'b' - binario.
# Los archivos se generan en el directorio en el que estamos trabajando a menos que se le indique lo contrario.
# Si el archivo no existe y utilizamos el modo 'w', python lo crea.
# En modo 'w' reemplaza todo el contenido del archivo.
# En modo 'w+' reemplaza solo la cantidad de bytes del contenido agregado en el contenido que tenia el archivo dejando el resto de lo anterior si el nuevo contenido es mas corto que el anterior.
# En modo 'a', añade el contenido a continuación del contenido anterior.

archivo = open('utils/EjemploManejoArchivos.txt', 'w')
archivo.write('Hoy estamos trabajando con archivos!\n')
archivo.close() # Siempre debemos cerrar el archivo.

# Permite matener el archivo abierto todo lo que dura el bloque de codigo, luego lo cierra automáticamente.
with open('utils/EjemploManejoArchivos.txt', 'w') as archivo:
    for i in range(1, 11):
        archivo.write(f'Linea N°{i}.\n')

with open('utils/EjemploManejoArchivos.txt', 'r') as archivo:
    for linea in archivo:
        print(linea, end='') # Indica a la función que el final de la lina se interpretada como un texto vacio en vez de '\n'

# Siguiente clase --> 46 Filtrar y buscar Archivos.
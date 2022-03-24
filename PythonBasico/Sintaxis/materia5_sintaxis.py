# 18. DICCIONARIOS: ----------------------------------------------------------------------------------------
# Elementos compuestos por pares clave-valor.
# Tanto claves como valores pueden ser de cualquier tipo.
diccionario = {}
type(diccionario)
diccionario = {'clave': 'valor'}
diccionario = dict() #Crea un diccionario vacio
diccionario = dict([('clave1', 'valor1'), ('clave2', 'valor2')])

# Agrega un nuevo valor al diccionario: **************
diccionario.setdefault('clave3', 'valor3')
diccionario['clave4'] = 'valor4'
# Para hacer reemplazos de algun valor necesariamente lo hacemos con la notacion de corchetes.

# Obtener elementos.
diccionario['clave1']
diccionario.get('clave2')
diccionario.get('clave5', 'Devuelve esta cadena si el elemento no existe!')
# Si intento consultar un llave que no existe, da un error.

# Eliminar Elementos. ***************************
diccionario.pop('clave4')
diccionario.pop('clave5', 'Regresa este mensaje si no existe el elemento')
diccionario.popitem()# devuelve un elemento(tiene comportamiento de una pila) y luego lo elimina.

len(diccionario)
'clave5' in diccionario
 
diccionario.keys() #Regresa las llaves contenidas en el diccionario.
diccionario.values() #Regresa los valores asociados a las claves.
diccionario.items() #Regresa una lista con tuplas que contienen la clave y valor

cont = 0
for key, value in diccionario.items():
    cont += 1
    print(f'{cont}) {key}: {value}')

print(diccionario)

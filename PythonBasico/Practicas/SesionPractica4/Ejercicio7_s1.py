'''
Partiendo de dos listas con nombres, se requiere eliminar de la primera lista, los nombres
que existen en la segunda. Finalmente mostrar como queda la primera lista
'''
lista1 = ["carlos", "pedro", "jacinto", "andrea", "mariana", "andrea", "anne", "mariana", "karina"]
lista2 = ["andrea", "anne", "mariana"]

# Eliminamos los nombres de la lista 1 que estan en la lista2.
lista1 = [nombre for nombre in lista1 if nombre not in lista2]

# Imprimimos la lista1 actualizada.
print(f'\nSe han removido elementos, lista1 actualizada =  {lista1}\n')

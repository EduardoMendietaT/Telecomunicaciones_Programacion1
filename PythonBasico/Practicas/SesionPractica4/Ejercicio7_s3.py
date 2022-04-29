'''
Partiendo de dos listas con nombres, se requiere eliminar de la primera lista, los nombres
que existen en la segunda. Finalmente mostrar como queda la primera lista
'''
lista1 = ["carlos", "pedro", "jacinto", "andrea", "mariana", "andrea", "anne", "mariana", "karina"]
lista2 = ["andrea", "anne", "mariana"]

# Eliminamos los nombres de la lista 1 que estan en la lista2.
cont_removidos = 0
i = 0
while i < len(lista1):
    if lista1[i] in lista2:
        lista1.remove(lista1[i])
        cont_removidos += 1
        i -= 1
    i += 1

# Imprimimos la lista1 actualizada.
print(f'\nSe han removido {cont_removidos} elementos, lista1 actualizada =  {lista1}\n')

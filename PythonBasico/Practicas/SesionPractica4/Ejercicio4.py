'''
Se requiere mostrar en pantalla la siguiente información: se tienen 3 listas con información sobre nombres,
identificadores, y sueldos de varios usuarios.
Se requiere mostrar esta información de forma tabulada como en el ejemplo a continuación.
'''
# Listas con información previa de los usuarios.
nombres = ["juan", "pedro", "maria", "cecilia"]
ids = [1, 24, 22, 54, 65]
sueldos = [100.2, 433.22, 500.3, 700, 300.44]

# Imprimimos el encabezado de la tabla.
print('\n{:<20s} {:<20s} {:<20s}'.format('Usuario', 'ID', 'Sueldo'))

#Generamos el cuerpo de la tabla con informacion de las 3 listas anteriores.
separador_tabla = '-'*48
for i in range(len(nombres)):
    if i == 0: print(separador_tabla)
    print('{:<20s} {:<20d} {:<20.2f}'.format(nombres[i], ids[i], sueldos[i]))
    if i == len(nombres) - 1: print(separador_tabla)

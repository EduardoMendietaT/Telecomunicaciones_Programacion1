'''
Se requiere un programa para "obscurecer" un texto. Es decir, que la legibilidad del texto sea más
complicada ya que se intercambiarán caractéres, logrando de esta forma que el texto se modifique.
Para este ejercicio, se cambiarán los siguientes caractéres:
    - a por 0
    - e por x
    - m por 7
Por ejemplo la frase: "este auto necesita mantenimiento" debe ser cambiada a "xstx 0uto nxcxsit0 70ntxni7ixnto"
'''
texto = input('\nIngrese un texto para "obscurecer": ')

# Creamos un diccionario con los caracteres especiales a remplazar.
chars_especiales = {'a': '0', 'e': 'x',  'm': '7'}

# Creamos una lista con todas la palabras del texto original.
palabras = texto.split()

# Creamos una lista para almacenar las palabras modificadas.
palabras_obscurecidas = []

# Modiicamos el texto original tomando en cuenta que los caracteres especiales sen reemplazados.
for palabra in palabras:
    secreta = ''
    for i in palabra:
        secreta += i if not chars_especiales.get(i) else chars_especiales.get(i)
    palabras_obscurecidas.append(secreta)

# Reconstruimos el texto modificado e imprimimos por consola.
print(f'\nTexto "obscurecido": {" ".join(palabras_obscurecidas)}\n')

lista = ['dbdd47', 'dcaa37', 'dadd78', 'dbba37', 'acbb52', 'adad45', 'addd43', 'bbdb82', 'aaab22', 'bbac84', 'bcca83', 'adbc16', 'aabd48', 'abdb59', 'dbba51',
         'dbad46', 'cbca12', 'dccc66', 'dcba81', 'bbbc21', 'bbda25', 'abdb55', 'bbda36', 'aaad29', 'bdda17', 'aaab35', 'cacd19', 'adcc39', 'adbb87', 'bddc49',
         'abdd92', 'bdab35', 'acab81', 'babc89', 'bbba58', 'bcdc58', 'bcad98', 'dbdd52', 'cdac22', 'bbad38', 'adbc53', 'dcab49', 'ccad14', 'cbac43', 'cdcc54',
         'ddda27', 'ccca61', 'cbcd29', 'aacd26', 'dbcd57']

categorias = int(input("Ingrese las categorías: "))

inicio = 0
fin = 0

for i in range(categorias):
    elementos_cat = 0
    fin = fin + (99 // categorias)
    for y in lista:
        numero = int(y[4:])
        if inicio < numero and numero <= fin:
            elementos_cat += 1
    print("Categoria:", i+1, "Elementos: ", elementos_cat)
    inicio = fin

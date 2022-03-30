'''
Se requiere conocer el valor a pagar por consumo eléctrico. Para ello, se definen 
4 categorías de consumo, cada una con un valor diferente de costo de energía.
muestre los valores a pagar de varios clientes cuyas lecturas de consumo son las 
siguientes: 25, 10, 50, 34
'''
lecturas = [25, 10, 50, 34]

for i in lecturas:
    if i <= 20:
        valor_pagar = i * 10
    elif i <= 30:
        valor_pagar = i * 12
    elif i <= 40:
        valor_pagar = i * 15
    else:
        valor_pagar = i * 17
    print(f"Valor a pagar por consumir {i}w es ${valor_pagar} ")

# HASTA SLIDE 37 SESION 2:
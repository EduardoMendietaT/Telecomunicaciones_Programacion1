def calcular_costo(consumos):
    """Funcion que calcula el valor a pagar por un usuario, teniendo en cuenta el valor de consumo y la
    categoria del usuario

    Parametros
    ----------
    consumos : dict
      contiene los valores a pagar en el dia y la noche

    Retorna
    -------
    total_pagar : float
      valor a pagar por el consumo
    """
    # define una tarifa en dolares por consumo de energía
    tarifa = {
        "consumo_dia": 1.5,
        "consumo_noche": 1,
    }

    # Calculamos el valor a pagar
    total_pagar = 0
    for key, value in consumos.items():
        total_pagar += value * tarifa[key]

    return total_pagar


def imprimir_planilla(usuarios):
    """Imprimie la planilla con los valores a pagar por cada uno de los usuarios del diccionario `usuarios`

    Parametros
    ----------
    usuarios : dict
      diccionario con los usuarios y sus consumos
    """
    for key in usuarios.keys():
        total_pagar = calcular_costo(usuarios[key])
        print("{:20s}{:10.2f}".format(key, total_pagar))


# usuarios y sus consumos de día y de noche
usuarios = {
    "juan": {"consumo_dia": 100, "consumo_noche": 33},
    "carlos": {"consumo_dia": 200, "consumo_noche": 100},
    "maria": {"consumo_dia": 150, "consumo_noche": 76},
    "pedro": {"consumo_dia": 300, "consumo_noche": 200},
    "juana": {"consumo_dia": 22, "consumo_noche": 300},
}

# se llama a la funcion para imprimir la planilla de valores a pagarb
imprimir_planilla(usuarios)

def calcular_costo(consumo, horario, categoria):

    horarios = {"consumo_dia": 3, "consumo_noche": 1.5}
    tarifas = {"bajo": 3, "medio": 4, "alto": 5}

    return  consumo * tarifas[categoria] * horarios[horario]


def imprimir_planilla(usuarios):
    print("{:20s}{:10s}".format("Usuario", "Valor a pagar"))
    print("-"*35)

    for d in usuarios.keys():
        total = 0
        for k, v in usuarios[d].items():
            if v <= 100:
                categoria = "bajo"
            elif v <= 200:
                categoria = "medio"
            else:
                categoria = "alto"

            total += calcular_costo(v, k, categoria)
        print("{:20s}{:10.2f}".format(d, total))


usuarios = {
    "juan": {"consumo_dia": 100, "consumo_noche": 33},
    "carlos": {"consumo_dia": 200, "consumo_noche": 100},
    "maria": {"consumo_dia": 150, "consumo_noche": 76},
    "pedro": {"consumo_dia": 300, "consumo_noche": 200},
    "juana": {"consumo_dia": 22, "consumo_noche": 300},
}

imprimir_planilla(usuarios)
from automatos.automato_antigo import validar as validar_antigo
from automatos.automato_mercosul import validar as validar_mercosul
from automatos.automato_mercosul_convertido import validar as validar_convertido


def identificar_modelo(placa):
    placa = placa.upper().strip()

    if validar_antigo(placa):
        return "Modelo antigo"

    if validar_convertido(placa):
        return "Modelo antigo convertido para Mercosul"

    if validar_mercosul(placa):
        return "Modelo Mercosul"

    return "Placa inválida ou modelo não identificado"
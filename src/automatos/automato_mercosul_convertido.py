from automatos.automato_base import AutomatoFinito

transicoes = {
    ("q0", "L"): "q1",
    ("q1", "L"): "q2",
    ("q2", "L"): "q3",
    ("q3", "N"): "q4",
    ("q4", "L"): "q5",
    ("q5", "N"): "q6",
    ("q6", "N"): "q7",
}


def validar(placa):
    if len(placa) != 7 or placa[4] not in "ABCDEFGHIJ":
        return False

    automato = AutomatoFinito(
        transicoes=transicoes,
        estado_inicial="q0",
        estados_finais={"q7"}
    )

    return automato.executar(placa)
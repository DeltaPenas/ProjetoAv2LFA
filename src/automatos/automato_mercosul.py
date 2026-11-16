from automatos.automato_base import AutomatoFinito

# definição das transições para o comportamento do AFD
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
    automato = AutomatoFinito(transicoes=transicoes, estado_inicial="q0", estados_finais={"q7"})

    
    automato.imprimirEstados(placa)

    return automato.executar(placa)
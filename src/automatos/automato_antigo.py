from automatos.automato_base import AutomatoFinito



# definição das transições para o comportamento do AFD
transicoes = {
    ("q0", "L"): "q1",
    ("q1", "L"): "q2",
    ("q2", "L"): "q3",
    ("q3", "N"): "q5",
    ("q3", "H"): "q4",
    ("q4", "N"): "q5",
    ("q5", "N"): "q6",
    ("q6", "N"): "q7",
    ("q7", "N"): "q8",
}

# metodo de validação, recebe a placa, cria um automato e já define a transição e os estados, dps executa o metodo lá da classe automato_base

def validar(placa):
    automato = AutomatoFinito(
        transicoes=transicoes,
        estado_inicial="q0",
        estados_finais={"q8"}
    )
    return automato.executar(placa)
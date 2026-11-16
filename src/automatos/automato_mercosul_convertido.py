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

# metodo de validação, recebe a placa, cria um automato e já define a transição e os estados, dps executa o metodo lá da classe automato_base
# temos uma condicional que recebe a quarta posição e verifica se está entre  A-J, caso não esteja já retorna false

def validar(placa):
    if len(placa) != 7 or placa[4] not in "ABCDEFGHIJ":
        return False

    automato = AutomatoFinito(
        transicoes=transicoes,
        estado_inicial="q0",
        estados_finais={"q7"}
    )

    
    automato.imprimirEstados(placa)

    return automato.executar(placa)
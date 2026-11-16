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

    estado = "q0"
    # adicionei um laço for pra imprimir o caractere, simbulo, o estado atual e o proximo estado.
    for char in placa:
        simbulo = automato.classificar_char(char)
        proximo = automato.transicoes.get((estado, simbulo), automato.estado_rejeicao)
        print(f"Caractere: {char} / Símbolo: {simbulo} / {estado} > {proximo}")
        estado = proximo


    return automato.executar(placa)
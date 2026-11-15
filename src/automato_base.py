class AutomatoFinito:
        # Construtor, executado quando criamos um objeto de AutomatoFinito
        # transicoes: Armazena as regras de transição entre estados.
        # estado_inicial: Define onde a execução começa.
        # estados_finais: Define quais estados representam aceitação.
        # estado_rejeicao é definido diretamente dentro da classe \[M=(Q,\Sigma,\delta,q_0,F)\]
        
        def __init__(self, transicoes, estado_inicial, estados_finais):
                self.transicoes = transicoes
                self.estado_inicial = estado_inicial
                self.estados_finais = estados_finais
                self.estado_rejeicao = "qR"

        # Recebe o Char e identifica se ele é uma Letra (L), um numero (N) ou o Hifen (H), qualquer outra coisa retorna OUTRO.
        def classificar_char(self, char):
                if 'A' <= char <= 'Z':
                        return "L"
                elif '0' <= char <= '9':
                        return "N"
                elif char == '-':
                        return "H"
                else:
                        return "OUTRO"
        
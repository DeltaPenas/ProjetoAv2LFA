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


        # Parte principal da classe, percorre cada caractere da entrada, e retorna a categoria dele usando o metodo de classificação, O .get() 
        # consulta o dicionário de transições usando uma tupla: (estado_atual, simbolo) Se essa transição existir, o método retorna o próximo estado.
        #Se não existir, retorna qR, nosso estado de rejeição.

        def executar(self, entrada):
                estado_atual = self.estado_inicial

                for char in entrada:
                        sim = self.classificar_char(char)


                        estado_atual = self.transicoes.get((estado_atual, sim), self.estado_rejeicao)

                return estado_atual in self.estados_finais




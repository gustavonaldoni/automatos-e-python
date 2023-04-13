from af import AF
from afnd import AFND


class AFNDe(AF):
    def __init__(self):
        super().__init__()
        """
        Q
        Definição: conjunto de estados o qual é finito.
        Formato: {q0, q1, q2, ..., qn}, em que cada elemento é uma string.

        Sigma
        Definição: conjunto de símbolos aceitos pelo autômato (alfabeto).
        Formato: {s1, s2, s3, ..., sn}, em que cada elemento é uma string.

        Delta
        Definição: função programa.
        Formato: {(q, s) : p}, em que q é uma string pertencente a Q ou um movimento vazio representado pela string 'e', p é um subconjunto de Q e s é uma string pertencente a Sigma.

        q0
        Definição: estado inicial.
        Formato: q0, em que q0 é uma string pertencente a Q

        F
        Definição: conjunto de estados finais, sendo um subconjunto de Q.
        Formato: {q0, q1, q2, ..., qn}, em que cada elemento é uma string pertencente a Q.
        """

    def inserir_transicao(self, estado_inicial: str, simbolo: str, estados_resultantes: set):
        if estados_resultantes.issubset(self.Q) and estado_inicial in self.Q and (simbolo in self.Sigma or simbolo == ''):
            transicao = {(estado_inicial, simbolo): estados_resultantes}
            self.Delta.update(transicao)

    def mostrar(self):
        print(f'Q = {self.Q}')
        print(f'Σ = {self.Sigma}')

        print()
        for par, p in self.Delta.items():
            if len(p) == 0:
                print(f'δ({par[0]}, {par[1]}) = {{}}')
            else:
                print(f'δ({par[0]}, {par[1]}) = {p}')
        print()

        print(f'q0 = {self.q0}')
        print(f'F = {self.F}')
    
    def fecho_vazio(self, estado: str):
        if estado not in self.Q:
            return set()

        if self.Delta[(estado, '')] == set():
            return set({estado,})
        
        else:
            resultado = set({estado,})
            resultado.update(self.Delta[(estado, '')])

            for p in self.Delta[(estado, '')]:
                resultado.update(self.fecho_vazio(p))

                if resultado == self.Q:
                    return resultado
            
            return resultado

    def fecho_vazio_extendido(self, conjunto_de_estados: set):
        resultado = set()

        if conjunto_de_estados.issubset(self.Q) == False:
            return 0

        for estado in conjunto_de_estados:
            resultado.update(self.fecho_vazio(estado))
        
        return resultado

    def delta(self, estado: str, simbolo: str):
        if (estado not in self.Q) or (simbolo not in self.Sigma):
            return 0
        
        return self.Delta[(estado, simbolo)]
    
    def delta_extendido(self, conjunto_de_estados: set, simbolo: str):
        resultado = set()

        if conjunto_de_estados.issubset(self.Q) == False:
            return 0
        
        if simbolo not in self.Sigma:
            return 0

        for estado in conjunto_de_estados:
            resultado.update(self.delta(estado, simbolo))
        
        return resultado
    
    def delta_linha(self, estado: str, simbolo: str):
        if (estado not in self.Q) or (simbolo not in self.Sigma):
            return 0
        
        return self.fecho_vazio_extendido(self.delta_extendido(self.fecho_vazio(estado), simbolo))

    def achar_novos_estados_finais(self):
        resultado = set()

        for estado in self.Q:
            for q in self.fecho_vazio(estado):
                if q in self.F:
                    resultado.add(q)

        return resultado

    def converter_para_afnd(self):
        afnd = AFND()

        for estado in self.Q:
            afnd.inserir_estado(estado)
        
        for simbolo in self.Sigma:
            afnd.inserir_simbolo(simbolo)

        for estado in self.Q:
            for simbolo in self.Sigma:
                delta_linha = self.delta_linha(estado, simbolo)
                afnd.inserir_transicao(estado, simbolo, delta_linha)

        afnd.definir_estado_inicial(self.q0)

        novos_estados_finais = self.achar_novos_estados_finais()
        for estado in novos_estados_finais:
            afnd.definir_estado_final(estado)
        
        return afnd
        
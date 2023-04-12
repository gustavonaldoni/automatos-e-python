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
            elif par[1] == '':
                print(f'δ({par[0]}, ε) = {p}')
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
            
            return resultado

    def fecho_vazio_extendido(self, conjunto_de_estados: set):
        pass

    def converter_para_afnd(self):
        afnd = AFND()

        fechos_vazios = dict()
        for estado in self.Q:
            fechos_vazios.update({estado: self.fecho_vazio(estado)})

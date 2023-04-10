from afd import AFD


class AFND:
    def __init__(self):
        """
        Q
        Definição: conjunto de estados o qual é finito.
        Formato: {q0, q1, q2, ..., qn}, em que cada elemento é uma string.

        Sigma
        Definição: conjunto de símbolos aceitos pelo autômato (alfabeto).
        Formato: {s1, s2, s3, ..., sn}, em que cada elemento é uma string.

        Delta
        Definição: função programa.
        Formato: {(q, s) : p}, em que q é uma string pertencente a Q, p é um subconjunto de Q e s é uma string pertencente a Sigma.

        q0
        Definição: estado inicial.
        Formato: q0, em que q0 é uma string pertencente a Q

        F
        Definição: conjunto de estados finais, sendo um subconjunto de Q.
        Formato: {q0, q1, q2, ..., qn}, em que cada elemento é uma string pertencente a Q.
        """
        self.Q = set()
        self.Sigma = set()
        self.Delta = dict()
        self.q0 = 'q0'
        self.F = set()

    def inserir_estado(self, estado: str):
        self.Q.add(estado)

    def inserir_estados(self, *estados):
        for estado in estados:
            self.Q.add(estado)

    def definir_estado_inicial(self, estado: str):
        if estado in self.Q:
            self.q0 = estado

    def definir_estado_final(self, estado: str):
        if estado in self.Q:
            self.F.add(estado)

    def definir_estados_finais(self, *estados):
        for estado in estados:
            if estado in self.Q:
                self.F.add(estado)

    def inserir_simbolo(self, simbolo: str):
        self.Sigma.add(simbolo)

    def inserir_simbolos(self, *simbolos):
        for simbolo in simbolos:
            self.Sigma.add(simbolo)

    def inserir_transicao(self, estado_inicial: str, simbolo: str, estados_resultantes: set):
        if estados_resultantes.issubset(self.Q) and estado_inicial in self.Q and simbolo in self.Sigma:
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

    def funcao_caminho(self, caminho: set, simbolo: str):
        resultado = set()

        for estado in caminho:
            resultado.update(self.Delta[(estado, simbolo)]) 
        
        return tuple(resultado)

    def achar_novos_estados_finais(self, novos_estados: set):
        resultado = set()

        for novo_estado in novos_estados:
            for estado in novo_estado:
                if estado in self.F:
                    resultado.add(estado)

        return resultado

    def converter_para_afd(self):
        afd = AFD()

        novos_estados = set()
        novos_estados.add((self.q0,))
        
        novos_estados_aux = novos_estados.copy()

        while len(novos_estados) > 0:

            for estado in novos_estados:
                for simbolo in self.Sigma:
                    novo_estado = self.funcao_caminho(set(estado), simbolo)
                    novos_estados_aux.add(novo_estado) 

            n = novos_estados_aux.copy()
            n.difference_update(novos_estados)
            
            novos_estados = n.copy()
        
        if tuple() in novos_estados:
            novos_estados.remove(tuple())

        print(novos_estados)

            
            
        
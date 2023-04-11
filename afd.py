from af import AF


class AFD(AF):
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
        Formato: {(q1, s) : q2}, em que q1 e q2 são strings pertencentes a Q e s é uma string pertencente a Sigma.

        q0
        Definição: estado inicial.
        Formato: q0, em que q0 é uma string pertencente a Q

        F
        Definição: conjunto de estados finais, sendo um subconjunto de Q.
        Formato: {q0, q1, q2, ..., qn}, em que cada elemento é uma string pertencente a Q.
        """
        super().__init__()

    def inserir_transicao(self, estado_inicial: str, simbolo: str, estado_resultante: str):
        if estado_inicial in self.Q and (estado_resultante in self.Q or estado_resultante == '') and simbolo in self.Sigma:
            transicao = {(estado_inicial, simbolo): estado_resultante}
            self.Delta.update(transicao)

    def verificar(self, palavra: str):
        q0 = self.q0

        while palavra != "":
            if palavra[0] not in self.Sigma:
                return False

            q0 = self.Delta[(q0, palavra[0])]

            if q0 == '':
                return False

            palavra = palavra[1:]

        return (q0 in self.F)

    def mostrar(self):
        print(f'Q = {self.Q}')
        print(f'Σ = {self.Sigma}')

        print()
        for par, q2 in self.Delta.items():
            print(f'δ({par[0]}, {par[1]}) = {q2}')
        print()

        print(f'q0 = {self.q0}')
        print(f'F = {self.F}')

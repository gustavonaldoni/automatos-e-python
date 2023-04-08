class AFD:
    def __init__(self, Q: set, Sigma: set, Delta: dict, q0: int, F: set):
        """
        Q
        Definição: conjunto de estados o qual é finito.
        Formato: {0, 1, 2, ..., n}, em que cada elemento é um inteiro.

        Sigma
        Definição: conjunto de símbolos aceitos pelo autômato (alfabeto).
        Formato: {s1, s2, s3, ..., sn}, em que cada elemento é uma string.

        Delta
        Definição: função programa.
        Formato: {(q1, s) : q2}, em que q1 e q2 são inteiros pertencentes a Q e s é uma string pertencente a Sigma.

        q0
        Definição: estado inicial.
        Formato: q0, em que q0 é um número inteiro pertencente a Q

        F
        Definição: conjunto de estados finais, sendo um subconjunto de Q.
        Formato: {0, 1, 2, ..., n}, em que cada elemento é um inteiro pertencente a Q.
        """
        self.Q = Q
        self.Sigma = Sigma
        self.Delta = Delta
        self.q0 = q0
        self.F = F

    def verificar(self, palavra: str):
        q0 = self.q0

        while palavra != "":
            if palavra[0] not in self.Sigma:
                return False
            
            q0 = self.Delta[(q0, palavra[0])]

            if q0 == -1:
                return False

            palavra = palavra[1:]

        return (q0 in self.F)

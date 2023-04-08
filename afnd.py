class AFND:
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
        Formato: {(q1, s) : p}, em que q1 é um inteiro pertencente a Q, p é um subconjunto de Q e s é uma string pertencente a Sigma.

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
        r = set()

        try:
            q0 = self.Delta[(self.q0, palavra[0])]
        except:
            return False

        while palavra != "":
            if palavra[0] not in self.Sigma:
                return False

            if q0 == {-1}:
                return False

            for q in q0:
                r.update(self.Delta[(q, palavra[0])])

            palavra = palavra[1:]

        for qf in self.F:
            if qf in r:
                return True
        
        return False

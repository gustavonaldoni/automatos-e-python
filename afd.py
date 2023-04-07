class AFD:
    def __init__(self, Q: set, Sigma: set, Delta: dict, q0: int, F: set):
        self.Q = Q
        self.Sigma = Sigma
        self.Delta = Delta
        self.q0 = q0
        self.F = F

    def validar(self, palavra: str):
        q0 = self.q0

        while palavra != "":
            q0 = self.Delta[(q0, palavra[0])]

            if q0 == -1:
                return False

            palavra = palavra[1:]

        return (q0 in self.F)

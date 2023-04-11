class AF:
    def __init__(self):
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

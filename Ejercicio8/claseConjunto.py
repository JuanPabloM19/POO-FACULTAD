class Conjunto:
    def __init__(self, elementos):
        self.elementos = set(elementos)

    def __add__(self, otro_conjunto):
        union = self.elementos | otro_conjunto.elementos
        return Conjunto(union)

    def __sub__(self, otro_conjunto):
        diferencia = self.elementos - otro_conjunto.elementos
        return Conjunto(diferencia)

    def __eq__(self, otro_conjunto):
        return self.elementos == otro_conjunto.elementos

    def __str__(self):
        return "{" + ", ".join(map(str, self.elementos)) + "}"

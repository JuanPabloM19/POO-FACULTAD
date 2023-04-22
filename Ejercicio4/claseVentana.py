class Ventana:
    def __init__(self, titulo, x1=0, y1=0, x2=500, y2=500):
        self.titulo = titulo
        self.x1 = max(0, x1)
        self.y1 = max(0, y1)
        self.x2 = min(500, x2)
        self.y2 = min(500, y2)

    def mostrar(self):
        print(f"Ventana: {self.titulo} Coordenadas: ({self.x1}, {self.y1}) - ({self.x2}, {self.y2})")

    def getTitulo(self):
        return self.titulo

    def alto(self):
        return abs(self.y2 - self.y1)

    def ancho(self):
        return abs(self.x2 - self.x1)

    def moverDerecha(self, unidades=1):
        self.x1 += unidades
        self.x2 += unidades

    def moverIzquierda(self, unidades=1):
        self.x1 -= unidades
        self.x2 -= unidades

    def bajar(self, unidades=1):
        self.y1 += unidades
        self.y2 += unidades

    def subir(self, unidades=1):
        self.y1 -= unidades
        self.y2 -= unidades
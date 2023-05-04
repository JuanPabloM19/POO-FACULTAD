class Ventana:
    __titulo = ""
    __x1 = ""
    __x2 = ""
    __y1 = ""
    __y2 = ""
    def __init__(self, titulo="", x1=0, y1=0, x2=500, y2=500):
        self.__titulo = titulo
        self.__x1 = max(0, x1)
        self.__y1 = max(0, y1)
        self.__x2 = min(500, x2)
        self.__y2 = min(500, y2)

    def mostrar(self):
        print(f"Ventana: {self.__titulo} Coordenadas: ({self.__x1}, {self.__y1}) - ({self.__x2}, {self.__y2})")

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return abs(self.__y2 - self.__y1)

    def ancho(self):
        return abs(self.__x2 - self.__x1)

    def moverDerecha(self, unidades=1):
        self.__x1 += unidades
        self.__x2 += unidades

    def moverIzquierda(self, unidades=1):
        self.__x1 -= unidades
        self.__x2 -= unidades

    def bajar(self, unidades=1):
        self.__y1 += unidades
        self.__y2 += unidades

    def subir(self, unidades=1):
        self.__y1 -= unidades
        self.__y2 -= unidades
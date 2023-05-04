class ViajeroFrecuente:
    __num_viajero = ""
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acumuladas = ""

    def __gt__(self, otro_viajero):
        return self.__millas_acumuladas > otro_viajero.__millas_acumuladas

    def __add__(self, millas_recorridas):
        self.__millas_acumuladas += millas_recorridas
        return self

    def __sub__(self, millas_a_canjear):
        if millas_a_canjear <= self.__millas_acumuladas:
            self.__millas_acumuladas -= millas_a_canjear
        else:
            print("Error: No se pueden canjear más millas de las acumuladas.")
        return self
    
    def __init__(self, num_viajero="", dni="", nombre="", apellido="", millas_acumuladas=""):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acumuladas = millas_acumuladas

    def cantidad_total_de_millas(self):
        return self.__millas_acumuladas

    def acumular_millas(self, millas_recorridas):
        self.__millas_acumuladas += millas_recorridas
        return self.__millas_acumuladas

    def canjear_millas(self, millas_a_canjear):
        if millas_a_canjear <= self.__millas_acumuladas:
            self.__millas_acumuladas -= millas_a_canjear
            return self.__millas_acumuladas
        else:
            print("Error: No se pueden canjear más millas de las acumuladas.")
            return self.__millas_acumuladas

    def get_num_viajero(self):
        return self.__num_viajero
    
    def get_millas_acumuladas(self):
        return self.__millas_acumuladas
    
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido
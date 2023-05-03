class ViajeroFrecuente:
    __num_viajero = ""
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acumuladas = ""

    def __gt__(self, otro_viajero):
        return self.millas_acumuladas > otro_viajero.millas_acumuladas

    def __add__(self, millas_recorridas):
        self.millas_acumuladas += millas_recorridas
        return self

    def __sub__(self, millas_a_canjear):
        if millas_a_canjear <= self.millas_acumuladas:
            self.millas_acumuladas -= millas_a_canjear
        else:
            print("Error: No se pueden canjear más millas de las acumuladas.")
        return self
    
    def __init__(self, num_viajero, dni, nombre, apellido, millas_acumuladas):
        self.num_viajero = num_viajero
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.millas_acumuladas = millas_acumuladas

    def cantidad_total_de_millas(self):
        return self.millas_acumuladas

    def acumular_millas(self, millas_recorridas):
        self.millas_acumuladas += millas_recorridas
        return self.millas_acumuladas

    def canjear_millas(self, millas_a_canjear):
        if millas_a_canjear <= self.millas_acumuladas:
            self.millas_acumuladas -= millas_a_canjear
            return self.millas_acumuladas
        else:
            print("Error: No se pueden canjear más millas de las acumuladas.")
            return self.millas_acumuladas

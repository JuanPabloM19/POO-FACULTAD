class PlanAhorro:
    __codigo = ""
    __modelo = ""
    __version = ""
    __valor_vehiculo = ""
    cantidad_cuotas = 60
    cuotas_licitar = 10

    def __init__(self, codigo="", modelo="", version="", valor_vehiculo=""):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor_vehiculo = valor_vehiculo

    @staticmethod
    def set_datos_estaticos(cantidad_cuotas, cuotas_licitar):
        PlanAhorro.cantidad_cuotas = cantidad_cuotas
        PlanAhorro.cuotas_licitar = cuotas_licitar

    def actualizar_valor_vehiculo(self, nuevo_valor):
        self.__valor_vehiculo = nuevo_valor

    def valor_cuota(self):
        return (self.__valor_vehiculo / PlanAhorro.cantidad_cuotas) + (self.__valor_vehiculo * 0.10)

    def monto_licitar(self):
        return PlanAhorro.cuotas_licitar * self.valor_cuota()

    def __str__(self):
        return f"Código: {self.__codigo}, Modelo: {self.__modelo}, Versión: {self.__version}, Valor Vehículo: {self.__valor_vehiculo}"

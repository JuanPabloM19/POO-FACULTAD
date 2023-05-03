class PlanAhorro:
    __codigo = ""
    __modelo = ""
    __version = ""
    __valor_vehiculo = ""
    cantidad_cuotas = 60
    cuotas_licitar = 10

    def __init__(self, codigo, modelo, version, valor_vehiculo):
        self.codigo = codigo
        self.modelo = modelo
        self.version = version
        self.valor_vehiculo = valor_vehiculo

    @staticmethod
    def set_datos_estaticos(cantidad_cuotas, cuotas_licitar):
        PlanAhorro.cantidad_cuotas = cantidad_cuotas
        PlanAhorro.cuotas_licitar = cuotas_licitar

    def actualizar_valor_vehiculo(self, nuevo_valor):
        self.valor_vehiculo = nuevo_valor

    def valor_cuota(self):
        return (self.valor_vehiculo / PlanAhorro.cantidad_cuotas) + (self.valor_vehiculo * 0.10)

    def monto_licitar(self):
        return PlanAhorro.cuotas_licitar * self.valor_cuota()

    def __str__(self):
        return f"Código: {self.codigo}, Modelo: {self.modelo}, Versión: {self.version}, Valor Vehículo: {self.valor_vehiculo}"

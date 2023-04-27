import csv

class PlanAhorro:
    cantidad_cuotas = 0
    cuotas_para_licitar = 0

    def __init__(self, codigo, modelo, version, valor_vehiculo):
        self.codigo = codigo
        self.modelo = modelo
        self.version = version
        self.valor_vehiculo = valor_vehiculo

    def calcular_valor_cuota(self):
        return (self.valor_vehiculo / PlanAhorro.cantidad_cuotas) + (self.valor_vehiculo * 0.10)

    def monto_para_licitar(self):
        return PlanAhorro.cuotas_para_licitar * self.calcular_valor_cuota()
    
    def actualizar_valor_vehiculo(plan):
        print(f"Código del plan: {plan.codigo}, Modelo: {plan.modelo}, Versión: {plan.version}")
        nuevo_valor = float(input("Ingrese el valor actual del vehículo: "))
        plan.valor_vehiculo = nuevo_valor

    def mostrar_planes_con_cuota_inferior_a(planes, valor):
        for plan in planes:
            if plan.calcular_valor_cuota() < valor:
                print(f"Código del plan: {plan.codigo}, Modelo: {plan.modelo}, Versión: {plan.version}")

    def modificar_cuotas_para_licitar(codigo, nueva_cantidad):
        PlanAhorro.cuotas_para_licitar = nueva_cantidad

    def leer_planes_desde_archivo(nombre_archivo):
        planes = []
        with open("planes.csv", "r") as archivo:
            for linea in archivo:
                codigo, modelo, version, valor_vehiculo = linea.strip().split(";")
                plan = PlanAhorro(codigo, modelo, version, float(valor_vehiculo))
                planes.append(plan)
        return planes


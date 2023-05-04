import csv
from clasePlanAhorro import PlanAhorro

def leer_planes_ahorro(archivo):
    planes = []
    with open("planes.csv", "r") as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            codigo, modelo, version, valor_vehiculo, cantidad_cuotas, cuotas_licitar = row
            plan = PlanAhorro(codigo, modelo, version, float(valor_vehiculo))
            planes.append(plan)
    return planes

def mostrar_menu():
    print("Menú de opciones:")
    print("1. Actualizar el valor del vehículo de cada plan.")
    print("2. Mostrar planes con cuota inferior al valor dado.")
    print("3. Mostrar el monto que se debe haber pagado para licitar el vehículo.")
    print("4. Modificar la cantidad de cuotas que debe tener pagas para licitar.")
    print("0. Salir")

def main():
    PlanAhorro.set_datos_estaticos(48, 24)
    planes = leer_planes_ahorro("planes_ahorro.csv")

    while True:
        mostrar_menu()
        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 1:
            for plan in planes:
                print(plan)
                nuevo_valor = float(input("Ingrese el nuevo valor del vehículo: "))
                plan.actualizar_valor_vehiculo(nuevo_valor)
        elif opcion == 2:
            valor = float(input("Ingrese el valor para comparar: "))
            for plan in planes:
                if plan.valor_cuota() < valor:
                    print(plan)
        elif opcion == 3:
            for plan in planes:
                print(plan)
                print(f"Monto para licitar: {plan.monto_licitar()}")
        elif opcion == 4:
            codigo = input("Ingrese el código del plan: ")
            for plan in planes:
                if plan.get_codigo() == codigo:
                    nuevas_cuotas = int(input("Ingrese la nueva cantidad de cuotas para licitar: "))
                    PlanAhorro.set_datos_estaticos(PlanAhorro.cantidad_cuotas, nuevas_cuotas)
                    break
            else:
                print("Código no encontrado.")
        elif opcion == 0:
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()

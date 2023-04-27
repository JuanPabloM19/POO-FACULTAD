from clasePlanAhorro import PlanAhorro

import csv

def main():
    planes = leer_planes_desde_archivo("planes.csv")

    while True:
        print("\nMenú de opciones:")
        print("1. Actualizar el valor del vehículo de cada plan")
        print("2. Mostrar planes con cuota inferior a un valor dado")
        print("3. Mostrar el monto para licitar el vehículo")
        print("4. Modificar la cantidad de cuotas para licitar")
        print("5. Salir")

        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 1:
            for plan in planes:
                actualizar_valor_vehiculo(plan)
        elif opcion == 2:
            valor = float(input("Ingrese el valor de referencia: "))
            mostrar_planes_con_cuota_inferior_a(planes, valor)
        elif opcion == 3:
            for plan in planes:
                print(f"Monto para licitar el vehículo del plan {plan.codigo}: {plan.monto_para_licitar()}")
        elif opcion == 4:
            codigo = input("Ingrese el código del plan: ")
            nueva_cantidad = int(input("Ingrese la nueva cantidad de cuotas para licitar: "))
            modificar_cuotas_para_licitar(codigo, nueva_cantidad)
        elif opcion == 5:
            break
        else:
            print("Opción inválida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()

import csv
from claseRegistro import Registro

def main():
    registros = leer_archivo("archivo_datos.csv")
    lista_bidimensional = almacenar_registros(registros)

    while True:
        print("Menú de opciones:")
        print("1. Mostrar valores extremos")
        print("2. Calcular promedio de temperatura por hora")
        print("3. Listar valores de un día")
        print("4. Salir")

        opcion = int(input("Ingrese el número de la opción deseada: "))

        if opcion == 1:
            mostrar_valores_extremos(lista_bidimensional)
        elif opcion == 2:
            calcular_promedio_temperatura_por_hora(lista_bidimensional)
        elif opcion == 3:
            dia = int(input("Ingrese el número de día: "))
            listar_valores_dia(dia, lista_bidimensional)
        elif opcion == 4:
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
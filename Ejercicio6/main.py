import csv
from claseViajero import ViajeroFrecuente

viajeros = []
with open("viajeros.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        num_viajero, dni, nombre, apellido, millas_acumuladas = row
        viajero = ViajeroFrecuente(num_viajero, dni, nombre, apellido, int(millas_acumuladas))
        viajeros.append(viajero)

def menu():
    print("Opciones:")
    print("a - Consultar Cantidad de Millas")
    print("b - Acumular Millas")
    print("c - Canjear Millas")
    print("d - Mostrar Viajero/s con Mayor Cantidad de Millas Acumuladas")
    print("q - Salir")

def buscar_viajero(num_viajero):
    for viajero in viajeros:
        if viajero.get_num_viajero() == num_viajero:
            return viajero
    return None

def viajero_con_mas_millas(viajeros):
    max_millas = max(viajeros, key=lambda v: v.get_millas_acumuladas())
    return [v for v in viajeros if v.get_millas_acumuladas() == max_millas.get_millas_acumuladas()]

def mostrar_viajeros_con_mas_millas(viajeros):
    viajeros_max_millas = viajero_con_mas_millas(viajeros)
    print("Viajeros con mayor cantidad de millas acumuladas:")
    for v in viajeros_max_millas:
        print(f"{v.get_nombre()} {v.get_apellido()} ({v.get_num_viajero()}): {v.get_millas_acumuladas()} millas")

while True:
    menu()
    opcion = input("Ingrese una opción: ")

    if opcion == 'q':
        break

    if opcion == 'd':
        mostrar_viajeros_con_mas_millas(viajeros)
        continue

    num_viajero = input("Ingrese el número de viajero frecuente: ")
    viajero = buscar_viajero(num_viajero)

    if viajero is None:
        print("No se encontró el viajero frecuente.")
        continue

    if opcion == 'a':
        print("Cantidad de millas acumuladas:", viajero.cantidad_total_de_millas())
    elif opcion == 'b':
        millas_recorridas = int(input("Ingrese la cantidad de millas recorridas: "))
        viajero += millas_recorridas  # Uso de la sobrecarga del operador suma
        print("Nuevo total de millas acumuladas:", viajero.get_millas_acumuladas())
    elif opcion == 'c':
        millas_a_canjear = int(input("Ingrese la cantidad de millas a canjear: "))
        viajero -= millas_a_canjear  # Uso de la sobrecarga del operador resta
        print("Nuevo total de millas acumuladas:", viajero.get_millas_acumuladas())
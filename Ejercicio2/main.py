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
    print("q - Salir")

def buscar_viajero(num_viajero):
    for viajero in viajeros:
        if viajero.num_viajero == num_viajero:
            return viajero
    return None

while True:
    menu()
    opcion = input("Ingrese una opción: ")

    if opcion == 'q':
        break

    num_viajero = input("Ingrese el número de viajero frecuente: ")
    viajero = buscar_viajero(num_viajero)

    if viajero is None:
        print("No se encontró el viajero frecuente.")
        continue

    if opcion == 'a':
        print("Cantidad de millas acumuladas:", viajero.cantidad_total_de_millas())
    elif opcion == 'b':
        millas_recorridas = int(input("Ingrese la cantidad de millas recorridas: "))
        print("Nuevo total de millas acumuladas:", viajero.acumular_millas(millas_recorridas))
    elif opcion == 'c':
        millas_a_canjear = int(input("Ingrese la cantidad de millas a canjear: "))
        print("Nuevo total de millas acumuladas:", viajero.canjear_millas(millas_a_canjear))
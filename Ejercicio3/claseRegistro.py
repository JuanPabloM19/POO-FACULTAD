import numpy as np

class Registro:
    __temperatura = ""
    __humedad = ""
    __presion_atmosferica = ""

    def __init__(self, temperatura, humedad, presion_atmosferica):
        self.temperatura = temperatura
        self.humedad = humedad
        self.presion_atmosferica = presion_atmosferica

    registros_mensuales = [[None for _ in range(24)] for _ in range(31)]

    def cargar_datos(archivo):
        with open(archivo, "r") as f:
            for linea in f:
                dia, hora, temperatura, humedad, presion = map(float, linea.strip().split(","))
                registros_mensuales[int(dia) - 1][int(hora)] = Registro(temperatura, humedad, presion)

    archivo = "datos_meteorologicos.txt"
    cargar_datos(archivo)

    import csv

    # Inicializar la lista bidimensional
    datos_mes = [[None for _ in range(24)] for _ in range(31)]

    # Leer el archivo y almacenar los datos en la lista bidimensional
    with open("datos_meteorologicos.csv", "r") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            dia, hora, temp, hum, pres = map(float, fila)
            dia, hora = int(dia) - 1, int(hora) # Ajustar a índices de la lista bidimensional
            datos_mes[dia][hora] = Registro(temp, hum, pres)

    # Función para mostrar el menú de opciones
    def mostrar_menu():
        print("Opciones:")
        print("1. Mostrar día y hora de menor y mayor valor para cada variable.")
        print("2. Indicar la temperatura promedio mensual por cada hora.")
        print("3. Listar valores de las tres variables para cada hora de un día específico.")
        print("4. Salir")

    # Funciones para realizar las tareas solicitadas
    def tarea_1():
        # Implementar lógica para encontrar el día y hora de menor y mayor valor para cada variable

    def tarea_2():
        # Implementar lógica para calcular la temperatura promedio mensual por cada hora

    def tarea_3(dia):
        # Implementar lógica para listar los valores de las tres variables para cada hora del día dado

    # Bucle principal del programa
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
    
        if opcion == 1:
            tarea_1()
        elif opcion == 2:
            tarea_2()
        elif opcion == 3:
            dia = int(input("Ingrese el número de día: "))
            tarea_3(dia)
        elif opcion == 4:
            break
        else:
            print("Opción inválida, por favor intente nuevamente.")


    def mostrar_menores_mayores(registros):
        menor_temperatura = np.min([[registro.temperatura for registro in fila] for fila in registros])
        mayor_temperatura = np.max([[registro.temperatura for registro in fila] for fila in registros])
        menor_humedad = np.min([[registro.humedad for registro in fila] for fila in registros])
        mayor_humedad = np.max([[registro.humedad for registro in fila] for fila in registros])
        menor_presion = np.min([[registro.presion_atmosferica for registro in fila] for fila in registros])
        mayor_presion = np.max([[registro.presion_atmosferica for registro in fila] for fila in registros])

        print("Menor temperatura:", menor_temperatura)
        print("Mayor temperatura:", mayor_temperatura)
        print("Menor humedad:", menor_humedad)
        print("Mayor humedad:", mayor_humedad)
        print("Menor presión atmosférica:", menor_presion)
        print("Mayor presión atmosférica:", mayor_presion)

    def temperatura_promedio_por_hora(registros):
        for hora in range(registros.shape[1]):
            suma_temperaturas = sum([registro.temperatura for registro in registros[:, hora]])
            promedio = suma_temperaturas / registros.shape[0]
            print("Hora", hora, "temperatura promedio:", promedio)

    def listar_valores_por_dia(registros, dia):
        print("Hora", "Temperatura", "Humedad", "Presión")
        for hora, registro in enumerate(registros[dia - 1]):
            print(hora, registro.temperatura, registro.humedad, registro.presion_atmosferica)

    while True:
        print("Menú de opciones:")
        print("1. Mostrar menor y mayor valor de cada variable")
        print("2. Temperatura promedio mensual por hora")
        print("3. Listar valores de un día específico")
        print("4. Salir")

        opcion = int(input("Seleccione una opción: "))
    
        if opcion == 1:
            mostrar_menores_mayores()
        elif opcion == 2:
            temperatura_promedio_por_hora()
        elif opcion == 3:
            dia = int(input("Ingrese el número de día: "))
            listar_valores_por_dia(dia)
        elif opcion == 4:
            break
        else:
            print("Opción inválida")
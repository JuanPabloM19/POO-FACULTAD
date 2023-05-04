class Registro:
    __temperatura = ""
    __humedad = ""
    __presion_atmosferica = ""
    def __init__(self, temperatura="", humedad="", presion_atmosferica=""):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion_atmosferica = presion_atmosferica

    def leer_archivo(nombre_archivo):
        registros = []
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                dia, hora, temperatura, humedad, presion = linea.strip().split(",")
                registros.append(((int(dia), int(hora)), Registro(float(temperatura), float(humedad), float(presion))))
        return registros

    def almacenar_registros(registros):
        lista_bidimensional = [[None for _ in range(24)] for _ in range(31)]
        for (dia, hora), registro in registros:
            lista_bidimensional[dia - 1][hora] = registro
        return lista_bidimensional

    def mostrar_valores_extremos(lista_bidimensional):
        min_temperatura = max_temperatura = lista_bidimensional[0][0].temperatura
        min_humedad = max_humedad = lista_bidimensional[0][0].humedad
        min_presion = max_presion = lista_bidimensional[0][0].presion_atmosferica
        min_temp_coords = max_temp_coords = min_hum_coords = max_hum_coords = min_pres_coords = max_pres_coords = (0, 0)
    
        for dia in range(31):
            for hora in range(24):
                registro = lista_bidimensional[dia][hora]
                if registro.temperatura < min_temperatura:
                    min_temperatura = registro.temperatura
                    min_temp_coords = (dia + 1, hora)
                if registro.temperatura > max_temperatura:
                    max_temperatura = registro.temperatura
                    max_temp_coords = (dia + 1, hora)
                if registro.humedad < min_humedad:
                    min_humedad = registro.humedad
                    min_hum_coords = (dia + 1, hora)
                if registro.humedad > max_humedad:
                    max_humedad = registro.humedad
                    max_hum_coords = (dia + 1, hora)
                if registro.presion_atmosferica < min_presion:
                    min_presion = registro.presion_atmosferica
                    min_pres_coords = (dia + 1, hora)
                if registro.presion_atmosferica > max_presion:
                    max_presion = registro.presion_atmosferica
                    max_pres_coords = (dia + 1, hora)
    
        print(f"Temperatura mínima: {min_temperatura} en el día {min_temp_coords[0]}, hora {min_temp_coords[1]}")
        print(f"Temperatura máxima: {max_temperatura} en el día {max_temp_coords[0]}, hora {max_temp_coords[1]}")
        print(f"Humedad mínima: {min_humedad} en el día {min_hum_coords[0]}, hora {min_hum_coords[1]}")
        print(f"Humedad máxima: {max_humedad} en el día {max_hum_coords[0]}, hora {max_hum_coords[1]}")
        print(f"Presión mínima: {min_presion} en el día {min_pres_coords[0]}, hora {min_pres_coords[1]}")
        print(f"Presión máxima: {max_presion} en el día {max_pres_coords[0]}, hora {max_pres_coords[1]}")

    def calcular_promedio_temperatura_por_hora(lista_bidimensional):
        suma_temperaturas = [0] * 24
        contador = [0] * 24
        for dia in range(31):
            for hora in range(24):
                suma_temperaturas[hora] += lista_bidimensional[dia][hora].temperatura
                contador[hora] += 1
    
        promedios = [suma_temperaturas[i] / contador[i] for i in range(24)]
    
        print("Temperatura promedio mensual por cada hora:")
        for hora, promedio in enumerate(promedios):
            print(f"{hora}: {promedio}")

    def listar_valores_dia(dia, lista_bidimensional):
        print("Hora\nTemperatura\nHumedad\nPresión")
        for hora in range(24):
            registro = lista_bidimensional[dia - 1][hora]
            print(f"{hora}\n{registro.temperatura}\n{registro.humedad}\n{registro.presion_atmosferica}")

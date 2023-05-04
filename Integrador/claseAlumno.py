class Alumno:
    __dni =""
    __apellido =""
    __nombre ="" 
    __carrera ="" 
    __anio_cursa ="" 
    def __init__(self, dni="", apellido="", nombre="", carrera="", anioquecursa=""):
        self.__dni = int(dni)
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__anio_cursa = int(anioquecursa)

    def __lt__(self, otro_alumno):
        if self.__anio_cursa != otro_alumno.__anio_cursa:
            return self.__anio_cursa < otro_alumno.__anio_cursa
        else:
            if self.__apellido != otro_alumno.__apellido:
                return self.__apellido < otro_alumno.__apellido
            else:
                return self.__nombre < otro_alumno.__nombre

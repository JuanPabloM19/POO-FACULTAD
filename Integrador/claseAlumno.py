class Alumno:
    def __init__(self, dni, apellido, nombre, carrera, anioquecursa):
        self.dni = int(dni)
        self.apellido = apellido
        self.nombre = nombre
        self.carrera = carrera
        self.anio_cursa = int(anioquecursa)

    def __lt__(self, otro_alumno):
        if self.anio_cursa != otro_alumno.anio_cursa:
            return self.anio_cursa < otro_alumno.anio_cursa
        else:
            if self.apellido != otro_alumno.apellido:
                return self.apellido < otro_alumno.apellido
            else:
                return self.nombre < otro_alumno.nombre

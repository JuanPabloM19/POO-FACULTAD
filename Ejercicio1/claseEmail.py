class Email:
    __idCuenta=""
    __dominio=""
    __tipo=""
    __contrasena=""

    def __init__(self,idCuenta="",dominio="",tipo="",contrasena=""):
        self.__idCuenta=idCuenta
        self.__dominio=dominio
        self.__tipo=tipo
        self.__contrasena=contrasena

    def retornaEmail(self):
        return self.__idCuenta + "@" + self.__dominio + "." + self.__tipo
    
    def getDominio(self):
        return self.__dominio

    def modificarContraseña(self, old):
        if old == self.__contrasena:
            self.__contrasena = str(input("Ingrese nueva contrasena "))
            print("Se cambio la contrasena")
        else:
            print("Las contraseñas no coinciden")
    
    def crearCuenta(self,email):
        email1 = email.split("@")
        self.__idCuenta = email1[0]
        email2 = email1[1].split(".")
        self.__dominio = email2[0]
        self.__tipo = email2[1]
        self.__contrasena = str(input("Ingrese contrasena "))
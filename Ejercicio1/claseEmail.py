import csv
class Email:
    __idCuenta = ""
    __dominio = ""
    __tipo = ""
    __contrasena = ""

    def __init__(self,idCuenta="",dominio="",tipo="",contrasena=""):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipo = tipo
        self.__contrasena = contrasena

    def getEmail(self):
        return self.__idCuenta + "@" + self.__dominio + "." + self.__tipo

    def getDominio(self):
        return self.__dominio
    
    def cambiarContrasena(self, contrasenaV):
        if(contrasenaV == self.__contrasena):
            self.__contrasena = str(input("Ingrese la nueva contrasena "))
        else:
            ("La contrasena ingresada no coincide con la creada.")

    def crearCuenta(self, email):
        emailParts = email.split("@")
        self.__idCuenta = emailParts[0]
        emailParts2 = emailParts[1].split(".")
        self.__dominio = emailParts2[0]
        self.__tipo = emailParts2[1]
        self.__contrasena = str(input("Ingrese contra"))
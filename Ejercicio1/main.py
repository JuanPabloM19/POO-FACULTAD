from claseEmail import Email
import csv

if __name__ == '__main__':
    
    nombre = input("Ingrese nombre ")
    idCuenta = input("Ingrese idCuenta ")
    dominio = input("Ingrese dominio ")
    tipo = input("Ingrese tipo ")
    contrasena = input("Ingrese contrasena ")
    emailInstance = Email(idCuenta, dominio, tipo, contrasena)
    print(f"Estimado {nombre} te enviaremos tus mensajes a la dirección " + emailInstance.retornaEmail())

    contrasenaA = str(input("Ingrese su contrasena actual "))
    emailInstance.modificarContraseña(contrasenaA)
    
    els = []
    with open("test1.csv", "r") as f:
        lines = f.readlines()
        for row in lines:
            row = row.strip()
            if "@" in row and "." in row:
                els.append(row)
            else:
                print(f"Dirección de email incorrecta: {row}")
        for email in els:
            emailInstance = Email()
            emailInstance.crearCuenta(email)
            print(emailInstance.retornaEmail())

    count = 0
    dominio = input("Ingrese dominio a buscar: ")
    for email in els:
        if dominio == emailInstance.getDominio():
            count = count + 1
    print(f"La cantidad de direcciones de correo con el dominio {dominio} es de {count}")

import csv
from claseEmail import Email

if __name__ == '__main__':
   
    nombre = input("Ingrese su nombre: ")
    idCuenta = input("Ingrese el id de la cuenta: ")
    dominio = input("Ingrese el dominio de la cuenta: ")
    tipo = input("Ingrese el tipo de dominio de la cuenta: ")
    contrasena = input("Ingrese la contrasena: ")
    emailInstance = Email(idCuenta, dominio, tipo, contrasena)
    print("Estimado " + nombre + ", le enviaremos sus mensajes a: " + emailInstance.getEmail())

    contrasenaActual = str(input("Ingrese su contrasena actual: "))
    emailInstance.cambiarContrasena(contrasenaActual)
    
    validEmails = []
    invalidEmails = []
    with open("test1.csv", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if "@" in line and "." in line:
                validEmails.append(line)
            else:
                invalidEmails.append(line)
        for email in validEmails:
            emailInstance = Email()
            emailInstance.crearCuenta(email)
            print(emailInstance.getEmail())
        for email in invalidEmails:
            print("Invalid " + email)

    count = 0
    dominio = input("Buscar dominio: ")
    for i in validEmails:
        if dominio == emailInstance.getDominio():
            count += 1
    print("La cantidad de objetos con el dominio %s es %d"%(dominio,count))
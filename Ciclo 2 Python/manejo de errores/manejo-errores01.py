from datetime import datetime


def leerFecha(msg):
    while True:
        try:
            # '%d/%m/%y' es dd/mm/yyyy
            fecha = datetime.strptime(input(msg), "%d/%m/%Y")
            ano, mes, dia = str(fecha).split()[0].split("-")
            return f"{dia}/{mes}/{ano}"
        except ValueError:
            print("Error. Formato de fecha inválido.\n")


def leerFloat(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except ValueError:
            print("Error. Ingrese un número decimal válido. \n")


def leerEntero(msg):
    while True:
        try:  # Hace lo que se le ponga abajo, a menos que haya un error y se llega al "except"
            num = int(input(msg))
            if num < 0:
                print("Error. Ingrese un numero positivo\n")
            else:
                return num
        except ValueError:  # hace lo que se le ponga abajo, por si llega a haber un error con lo que habia en el "try"
            print("Error. Ingrese un número entero válido.\n")

    return num


# temp = leerFloat("Ingrese la temperatura: ")

# print(temp, type(temp))

fecnac = leerFecha("Ingrese la fecha de nacimiento: ")
print(fecnac)

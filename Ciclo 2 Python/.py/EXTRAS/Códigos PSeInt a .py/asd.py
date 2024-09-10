def obtener_mes(opcion):
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    return meses.get(opcion, "Número fuera de rango")

def main():
    try:
        opcion = int(input("Ingresa un número del 1 al 12: "))
        mes = obtener_mes(opcion)
        print(f"El mes correspondiente es: {mes}")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")

if __name__ == "__main__":
    main()

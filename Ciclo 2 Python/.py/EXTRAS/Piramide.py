def generar_piramide_pascal(n):
    piramide = []

    for i in range(n):
        # Crear una nueva fila con 1 al inicio
        fila = [1] * (i + 1)

        # Calcular los valores de la fila excepto los extremos
        for j in range(1, i):
            fila[j] = piramide[i - 1][j - 1] + piramide[i - 1][j]

        # Agregar la fila a la pirámide
        piramide.append(fila)

    return piramide

# Imprimir la pirámide de Pascal
def imprimir_piramide(piramide):
    for fila in piramide:
        print(' '.join(map(str, fila)).center(2 * len(piramide)))

# Pedir al usuario el número de filas
n = int(input("Ingrese el número de filas de la pirámide de Pascal: "))

# Generar y mostrar la pirámide de Pascal
piramide = generar_piramide_pascal(n)
imprimir_piramide(piramide)

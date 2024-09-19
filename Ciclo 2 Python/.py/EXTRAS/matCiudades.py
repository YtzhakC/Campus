# Programa simple para verificar conexiones entre ciudades usando una matriz de adyacencia
def main():
    n = int(input("Ingrese el número de ciudades: "))
    
    # Entrada de los nombres de las ciudades
    ciudades = [input(f"Ciudad {i+1}: ") for i in range(n)]
    
    # Crear la matriz de adyacencia
    mat_ciudades = [[0] * n for f in range(n)]
    
    # Llenar la matriz con las conexiones
    for i in range(n):
        for j in range(i+1, n):
            if input(f"¿Hay conexión entre {ciudades[i]} y {ciudades[j]}? (si/no): ").strip().lower() == "si":
                mat_ciudades[i][j] = mat_ciudades[j][i] = 1

    # Verificar la conexión entre dos ciudades
    ciudad1 = input("Primera ciudad: ")
    ciudad2 = input("Segunda ciudad: ")
    
    # Comprobación de la conexión
    if ciudad1 in ciudades and ciudad2 in ciudades:
        i, j = ciudades.index(ciudad1), ciudades.index(ciudad2)
        print(f"Conexión directa: {'Sí' if mat_ciudades[i][j] == 1 else 'No'}")
    else:
        print("Una de las ciudades no está en la lista")

if __name__ == "__main__":
    main()

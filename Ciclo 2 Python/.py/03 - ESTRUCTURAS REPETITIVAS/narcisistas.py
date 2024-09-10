# Encontrar si un número es narcisista o no
# Es narcisistas si la suma de sus dígitos a la cantidad de dígitos es igual al número
# Ejemplo:
# 153 = 1^3 + 5^3 + 3^3

# Paso 1: Pedir el número
import math


n = int(input("Ingrese el número: \n"))
if n > 0:
    # Paso 2: Calcular la longitud del número
    lnum = int(math.log10(n)) + 1
    print("Longitud: ", lnum)

    # Paso 3: Sacar los dígitos del número y sumarlos elevándolos a la longitud del número
    suma = 0
    temp = n
    for i in range(1, lnum + 1):
        d = n % 10
        suma += d ** lnum
        n = n //10

    if suma == temp:
        print("El número es narciso.")
    else:
        print("El número no es narciso.")

else:
    print("Error. Ingrese un número entero positivo.")

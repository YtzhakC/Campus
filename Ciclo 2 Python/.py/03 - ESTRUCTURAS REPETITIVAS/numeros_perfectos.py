# Mostrar si un número es perfecto
# Un número es perfecto si la suma de sus divisores da el mismo número.

n = int(input("ingrese un número entero positivo mayor que 1: "))

if n > 1:
    suma = 0
    for d in range(1, n):
        if n % d == 0:
            suma += d # "suma = suma + d" es lo mismo que "suma += d"

    if suma == n:
        print("El número es perfecto.")
    else:
        print("El número no es perfecto.")
else:
    print(">> ERROR. Digite un número positivo mayor que 1")

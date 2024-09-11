import math 
def calcular_ex(x):
    n = 0
    result = 1
    suma = 0

    while result > 0.00001:

        suma += result

        n += 1

        result = (x ** n) / math.factorial(n)
    return suma

x = float(input("Ingrese el valor de x: \n-> "))

resultado = calcular_ex(x)

print(f"El valor aproximado de e^{x} es: {resultado:,}")

print('\n', math.exp(x))

# Dado la base y la altura de un triángulo, calcular y mostrar su área
# a través de la fórmula área = (base * altura)/2

# ENTRADA
# b: Base: float
# h: altura: float

b = float(input("Digite el valor de la base del triángulo: "))
h = float(input("Digite el valor de la altura del triángulo: "))
a = b * h / 2

# formateando la salida con format()
print("El área del triángulo es: {:.1f}". format(a))

# formateando la salida con cadenas f-string
print(f"El área del triángulo es: {a:.1f}")

# PROCESO
# a = b * h / 2

# SALIDA
# a: area: float

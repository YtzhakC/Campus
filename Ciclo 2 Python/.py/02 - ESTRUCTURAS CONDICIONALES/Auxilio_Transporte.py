# Auxilio de transporte según salario de un trabajador.
nick = input("Digite su nombre \n ")
salario = int(input("Digite sus ingresos mensuales \n$ "))
aux = 0

if salario <= 1_200_000:
    aux = 120_000

print("Nombre: ", nick)
print(f"Salario: {salario:,}")
print(f"El auxilio de transporte es de: ${aux:,} ")

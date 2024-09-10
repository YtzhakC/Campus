# INSTRUCCIÓN BREAK
# break: romper o terminar forzosamente el ciclo más cercano

# Sumar los números del 1 al 50
suma = 0
for i in range(1, 51):
    suma += i #Es equivalente a suma = suma + i
    if i == 20:
        break

print(suma)
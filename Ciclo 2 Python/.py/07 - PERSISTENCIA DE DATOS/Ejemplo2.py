import io

fd = open('Ciclo 2 Python/.py/07 - PERSISTENCIA DE DATOS/data.txt', 'r')

cad = fd.readline().strip()
print(cad)

cad = fd.readline().strip()
print(cad)

fd.close()

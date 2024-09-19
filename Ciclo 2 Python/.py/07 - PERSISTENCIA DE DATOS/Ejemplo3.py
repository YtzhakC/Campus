import io

fd = open('Ciclo 2 Python/.py/07 - PERSISTENCIA DE DATOS/data.txt', 'r')

cad = fd.readlines()
print(cad)

fd.close()

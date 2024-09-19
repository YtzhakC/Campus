import io

fd = open('Ciclo 2 Python/.py/07 - PERSISTENCIA DE DATOS/data.txt', 'r')

cad = fd.read()
print(cad)

fd.seek(0)
cad = fd.read(5)
print(cad)

fd.close()
import io  # noqa: F401

fd = open('Ciclo 2 Python/.py/07 - PERSISTENCIA DE DATOS/data.txt', 'r')

# RECORRIDO DE ARCHIVOS
for linea in fd:
    print(linea.strip().title())

fd.seek(0)

for caracter in fd.read():
    print(caracter.strip(), end=',')

fd.close()
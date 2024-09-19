# Contadores de líneas de archivos :D

fd = open('Ciclo 2 Python/.py/07 - PERSISTENCIA DE DATOS/Ejercicio Archivos MBox/mbox.txt', 'r')

cont = 0
for linea in fd: # Versión con FOR (Es más corto)
    if linea.startswith('From:'):
        cont += 1

print(cont)

# fd.seek(0)

# cont = 0
# linea = fd.readline()
# while linea: # Versión con WHILE (Es más largo)
#     cont += 1
#     linea = fd.readline()

# print(cont)

fd.close()
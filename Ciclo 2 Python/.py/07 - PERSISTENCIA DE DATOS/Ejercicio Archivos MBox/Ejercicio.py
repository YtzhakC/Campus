# Escriba un programa que envíe un mensaje: "Vota por mi mascota" a todos los correos que aparecen en el "From:"
# Su programa debe mostrar un mensaje como el siguiente por cada correo:
# cwen@iupi.edu --> "Vota por mi mascota" :::> [CORREO ENVIADO]

fd = open('Ciclo 2 Python/.py/07 - PERSISTENCIA DE DATOS/Ejercicio Archivos MBox/mbox.txt', 'r')

cont = 0

for linea in fd:
    if linea.startswith('From:'):
        print(linea.removeprefix('From:').strip('\n'), '--> Vota por mi mascota :::> [CORREO ENVIADO]')
        cont += 1

print(cont)

fd.close()

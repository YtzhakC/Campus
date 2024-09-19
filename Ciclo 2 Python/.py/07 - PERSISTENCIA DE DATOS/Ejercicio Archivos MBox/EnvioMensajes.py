with open('Ciclo 2 Python/.py/07 - PERSISTENCIA DE DATOS/Ejercicio Archivos MBox/mbox.txt', 'r') as fd:
    lstEmail = []
    for linea in fd:
        if linea.startswith('From:'):
            correo = linea.split()[1] + ': Enviado [OK] \n'
            if correo not in lstEmail:
                lstEmail.append(correo)

lstEmail.reverse()

with open('Ciclo 2 Python/.py/07 - PERSISTENCIA DE DATOS/Ejercicio Archivos MBox/correos_enviados.txt', 'w') as fd: # Se puede usar la misma porque anteriormente se cerró "fd".
    fd.writelines(lstEmail)
    
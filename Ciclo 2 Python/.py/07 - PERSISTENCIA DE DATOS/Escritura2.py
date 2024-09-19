
fd = open('Ciclo 2 Python/.py/07 - PERSISTENCIA DE DATOS/data2.txt', 'w')

lcad = ['Los pollitos dicen\n', 'Yo seré la mascota']
fd.writelines(lcad)


fd.close()
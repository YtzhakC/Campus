
fd = open('Ciclo 2 Python/.py/07 - PERSISTENCIA DE DATOS/data2.txt', 'a')

lcad = ['Nos vamos de asado\n', 'Invita Anderson\n']
fd.writelines(lcad)


fd.close()
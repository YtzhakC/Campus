# Indicar si un número es primo.

num = int(input('Número? \n'))

if num > 1:
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break

    if es_primo:
        print('Es primo.')
    else:
        print('No es primo.')

else:
    print('No es primo.')
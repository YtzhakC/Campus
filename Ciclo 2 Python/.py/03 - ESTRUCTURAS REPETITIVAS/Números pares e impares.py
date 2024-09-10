
num = int(input('\n Ingrese un número: \n'))
while num != -1:
    if num > 0:
        if num % 2 == 0:
            print('Es par.')
        else:
            print('Es impar.')
    
    num = int(input('\nIngrese un número: \n'))

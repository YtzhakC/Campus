
name = input('Digite su nombre: \n')
stratum = int(input('\nDigite su estrato: \n'))
continuar = True
while continuar:
    bfee = 0
    if stratum == 1:
        bfee = 10000
    elif stratum == 2:
        bfee = 15000
    elif stratum == 3:
        bfee = 30000
    elif stratum == 4:
        bfee = 50000
    elif stratum == 5:
        bfee = 65000

    print('\n', '=' * 40, '\n')
    print(f'Nombre: {name}')
    print(f'Tarifa básica: {bfee:,}')
    print('\n', '=' * 40, '\n')

    opc = input('\n>>> Desea Continuar? (S/N) \n')
    # continuar = opc == "S" or opc == "s"

    if opc == 'N' or opc == 'n':
        continuar = False
    else:
        print('\n', '-' * 40, '\n')
        name = input('Digite su nombre: \n')
        stratum = int(input('\n Digite su estrato:'))

n = int(input('Digite la cantidad de usuarios que se van a resgistrar \n'))
for i in range(n):
    code = int(input("Digite su código \n"))
name = input('Digite su nombre: \n')
status = input('Digite su estado de servicio (S o V): \n') # Vigente = Current, Suspendido = Suspended.
stratum = int(input('Digite su estrato (1 - 6): \n'))
consumption = float(input('Digite su consumo mensual (en cm3): \n'))

fee1 = 10_000
fee2 = 20_000
fee3 = 30_000
fee4 = 45_000
fee5 = 60_000
fee6 = 70_000
consumption_fee = consumption*200

if (status == "S" or status == "s"):
    print('No hay nada que pagar.')
elif (status == "V" or status == "v" and stratum == 1):
    stratum = fee1
    print('')
    print(f'Nombre: {name} ')
    print(f'Tarifa básica: {fee1:,}')
    print(f'Tarifa de consumo: {consumption*200:,}')
    print(f'Tarifa de Servicio: {fee1 + consumption_fee:,}')
elif (status == "V" or status == "v" and stratum == 2):
    stratum = fee2
    print('')
    print(f'Nombre: {name} ')
    print(f'Tarifa básica: {fee2:,}')
    print(f'Tarifa de consumo: {consumption*200:,}')
    print(f'Tarifa de Servicio: {fee2 + consumption_fee:,}')
elif (status == "V" or status == "v" and stratum == 3):
    stratum = fee3
    print('')
    print(f'Nombre: {name} ')
    print(f'Tarifa básica: {fee3:,}')
    print(f'Tarifa de consumo: {consumption*200:,}')
    print(f'Tarifa de Servicio: {fee3 + consumption_fee:,}')
elif (status == "V" or status == "v" and stratum == 4):
    stratum = fee4
    print('')
    print(f'Nombre: {name} ')
    print(f'Tarifa básica: {fee4:,}')
    print(f'Tarifa de consumo: {consumption*200:,}')
    print(f'Tarifa de Servicio: {fee4 + consumption_fee:,}')
elif (status == "V" or status == "v" and stratum == 5):
    stratum = fee5
    print('')
    print(f'Nombre: {name} ')
    print(f'Tarifa básica: {fee5:,}')
    print(f'Tarifa de consumo: {consumption*200:,}')
    print(f'Tarifa de Servicio: {fee5 + consumption_fee:,}')
elif (status == "V" or status == "v" and stratum == 6):
    stratum = fee6
    print('')
    print(f'Nombre: {name} ')
    print(f'Tarifa básica: {fee6:,}')
    print(f'Tarifa de consumo: {consumption*200:,}')
    print(f'Tarifa de Servicio: {fee6 + consumption_fee:,}')
else:
    print('>> ERROR. Por favor digite un dato válido para el estado de servicio (V or S).')
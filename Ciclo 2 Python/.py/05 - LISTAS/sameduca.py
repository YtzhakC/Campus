

# Programa principal

d_categoria = {1:25_000, 2:30_000, 3:40_000, 4:45_000, 5:60_000}
n = int(input('Cantidad de docentes? \n-> '))

docentes = {}
suma = 0
for i in range(n):
    print(f'\nDocente {i+1}')
    cedula = input('Cédula? \n-> ')
    dDatos = {}
    dDatos['nombre'] = input('Nombre? \n-> ')
    dDatos['categoria'] = int(input('Categoría (1 al 5): \n-> '))
    dDatos['horas_lab'] = int(input('Horas Laboradas? \n-> '))
    dDatos['honorarios'] = d_categoria[dDatos['categoria']] * dDatos['horas_lab']

    docentes[cedula] = dDatos
    suma += dDatos['honorarios']

# Informe
print('')
print(' ** INFORME **'.center(40))
print('')

# Recorrer el diccionario para imprimir el informe (Se recorre con las llaves).
for k, v in docentes.items():
    print('Nombre:', v['nombre'].title())
    print(f"Honorarios: {v['honorarios']:,}")
    print('-' * 30, '\n')

print('')
print('=' * 30)
print(f'Valor total de los Honorarios ${suma:,}')
print('=' * 30)

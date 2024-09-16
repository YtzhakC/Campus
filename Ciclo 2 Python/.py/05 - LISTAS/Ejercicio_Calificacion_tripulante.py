def aprobacion(nota1, nota2, nota3):
    app = nota1*0.30 + nota2*0.30 + nota3*0.40
    if app >= 3.0:
        return [f'{app:.2f}', 'Aprobado']
    else:
        return [f'{app:.2f}', 'No aprobado']

# Programa principal

n = int(input('Cantidad de Estudiantes? \n-> '))
codigo = 0
while codigo != 999:

    estudiante = {}
    suma = 0
    for i in range(n):
        print(f'\nEstudiante {i+1}')
        codigo = input('Código? \n-> ')
        dDatos = {}
        dDatos['codigo'] = codigo
        dDatos['nombre'] = input('Nombre? \n-> ')
        dDatos['nota_1'] = float(input('Nota 1? \n-> '))
        dDatos['nota_2'] = float(input('Nota 2? \n-> '))
        dDatos['nota_3'] = float(input('Nota 3? \n-> '))
        dDatos['nota_f'] = aprobacion(dDatos['nota_1'], dDatos['nota_2'], dDatos['nota_3'])

        estudiante[codigo] = dDatos
    

# Informe
print('')
print('='*40)
print(' ** INFORME **'.center(40))
print('='*40)
print('')

# Recorrer el diccionario para imprimir el informe (Se recorre con las llaves).
for k, v in estudiante.items():
    print(f"Código: {v['codigo']}")
    print('Nombre:', v['nombre'].title())
    print(f"Nota 1: {v['nota_1']}")
    print(f"Nota 2: {v['nota_2']}")
    print(f"Nota 3: {v['nota_3']}")
    print(f"Nota Final: {v['nota_f']}")
    print('-' * 30)
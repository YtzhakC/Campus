dDatos = {}
art = {}
suma = 0
n = int(input('Cantidad de artículos? \n-> '))
for i in range(n):
    print(f'\nArtículo {i+1}:')
    codigo = input('Código? \n-> ')
    
    dDatos['codigo'] = codigo
    dDatos['nombre'] = input('Nombre de articulo? \n-> ')
    dDatos['valor_u'] = float(input('Valor Unitario? \n-> '))
    dDatos['cantidad'] = int(input('Cantidad Comprada? \n-> '))
    dDatos['valor'] = dDatos['valor_u'] * dDatos['cantidad']
    art[codigo] = dDatos
    suma += dDatos['valor']

# Informe
print('')
print('='*40)
print(' ** INFORME **'.center(40))
print('='*40)
print('')

# Recorrer el diccionario para imprimir el informe (Se recorre con las llaves).
for k, v in art.items():
    print(f"Código: {v['codigo']}")
    print(f"Nombre: {v['nombre'].title()}")
    print(f"Valor unitario: {v['valor_u']:,.0f}")
    print(f"Cantidad: {v['cantidad']:,}")
    print(f"Valor final: {v['valor']:,.0f}")
    print('-' * 30)
print(f'El valor final de la compra es de: ${suma:,.0f}')
print('-' * 30)
print('')
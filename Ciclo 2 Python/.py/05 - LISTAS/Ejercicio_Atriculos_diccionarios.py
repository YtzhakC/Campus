dDatos = {}
art = {}
price = {}
suma = 0
n = int(input('Cantidad de artículos? \n-> '))
for i in range(n):
    print(f'\nArtículo {i+1}:')
    codigo = int(input('Código? \n-> '))
    
    dDatos['codigo'] = codigo
    dDatos['nombre'] = input('Nombre de articulo? \n-> ')
    dDatos['valor_u'] = float(input('Valor Unitario? \n-> '))
    dDatos['cantidad'] = int(input('Cantidad Comprada? \n-> '))
    dDatos['valor'] = dDatos['valor_u'] * dDatos['cantidad']
    art[codigo] = dDatos['nombre']
    price[codigo] = dDatos['valor']
    suma += dDatos['valor']

# Informe
print('')
print('='*40)
print(' ** FACTURA **'.center(40))
print('='*40)
print('')

# Recorrer el diccionario para imprimir el informe (Se recorre con las llaves).
for k, v in art.items():
    print(f"Código: {dDatos['codigo']}")
    print(f"Nombre: {dDatos['nombre'].title()}")
    print(f"Valor unitario: {dDatos['valor_u']:,.0f}")
    print(f"Cantidad: {dDatos['cantidad']:,}")
    print(f"Valor final: {dDatos['valor']:,.0f}")
    print('-' * 30)
print(f'El valor final de la compra es de: ${suma:,.0f}')
print('-' * 30)
print('')
print(art)
print(price)

matriz = [[100, 88, 92, 94, 85, 110, 118], 
           [30,  42, 31, 32, 38,  40,  37], 
           [23,  35, 39, 45, 55,  60,  61], 
           [45,  50, 56, 65, 47,  57,  68], 
           [18,  25, 33, 21, 22,  28,  32]]

precios = [1500, 5000, 6500, 2500, 22500]
dia_ventas = 0
suma_productos = 0
dia = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
for columna in range(7):
    producto = 0
    suma_productos = 0
    for fila in range(5):
        suma_productos += matriz[fila][columna] * precios[producto]
        producto += 1
    if suma_productos >= dia_ventas:
        dia_ventas = suma_productos
        i = columna

print(f'El dia con mayor venta fue el {dia[i]}, con una venta de {dia_ventas:,}')

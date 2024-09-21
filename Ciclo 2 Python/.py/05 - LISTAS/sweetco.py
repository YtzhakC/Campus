def prodMayIngSem(mat, lst):
    lsting = []
    for f in range(len(mat)):
        # suma = 0
        # for c in range(len(mat[f])):
        #     suma += mat[f][c] * lst[f]
        #     lsting.append(suma)
             lsting.append(sum(mat[f]) * lst[f])

    mayor = max(lsting)
    prod = lsting.index(mayor) + 1

    return [prod, mayor]

def diaMayVent(mat, lst):
    dia_ventas = 0
    suma_productos = 0
    dia = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    for columna in range(7):
        producto = 0
        suma_productos = 0
        for fila in range(5):
            suma_productos += (mat[fila][columna] * lst[producto])
            producto += 1
        if suma_productos >= dia_ventas:
            dia_ventas = suma_productos
            i = columna
    return [dia[i], dia_ventas]




lstPrecios = [1500, 5000, 6500, 2500, 22500]

matVtas = [[100, 88, 92, 94, 85, 110, 100], 
           [30,  42, 31, 32, 38,  40,  37], 
           [23,  35, 39, 45, 55,  60,  61], 
           [45,  50, 56, 65, 47,  57,  68], 
           [18,  25, 33, 21, 22,  28,  32]]

prod, ingrprod = prodMayIngSem(matVtas, lstPrecios)
dia, dia_ventas = diaMayVent(matVtas, lstPrecios)
print(f'El producto que genera más ingresos en la semana es: {prod} - Vendió: ${ingrprod:,}')
print(f'El dia con mayor venta fue el {dia}, con una venta de {dia_ventas:,}')

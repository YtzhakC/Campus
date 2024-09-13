
def posElemMayList(lst):
    mayor = lst[0]
    pos = 0
    for i in range(len(lst)):
        if lst[i] > mayor:
            mayor = lst[i]
            pos = i
    return [pos, mayor]

def posMayList(lst):
    mayor = lst[0]
    pos = 0
    for i in range(len(lst)):
        if lst[i] > mayor:
            mayor = lst[i]
            pos = i
    return pos

def menorLista(lst):
    menor = lst[0]
    for e in lst:
        if e < menor:
            menor = e
    return menor

def mayorLista(lst):
    mayor = lst[0]
    for e in lst:
        if e > mayor:
            mayor = e
    return mayor

def sumaLista(lst):
    suma = 0
    for e in lst:
        suma += e
    return suma

def imprimeLista(lst):
    for e in lst:
        print(e, end=' | ')
        print('')

lista_numero = [10, 15, 20, 30, 40]
print(type(lista_numero))
print(lista_numero)
# print(lista_numero[6])

print(lista_numero[-1])
print(lista_numero[-5])

# Recorre una lista
# 1. por sus posicionhes
for i in range(len(lista_numero)):
    print(lista_numero[i], end=', ')
print('')

for i in range(-1, -len(lista_numero)-1, -1):
    print(lista_numero[i], end='* ')
print('')

for i in range(len(lista_numero)-1, -1, -1):
    print(lista_numero[i], end='; ')
print('')

# 2. Por sus elementos
for e in lista_numero:
    print(e, end='| ')

# Llamando a una función. Se le pasa al lista
imprimeLista(lista_numero)

# Función que devuelve la suma de los elementos de la lista
print('La suma de los elementos de la lista es: ', sumaLista(lista_numero))

# Imprimir el mayor elemento de la lista
print('El mayor elemento es: ', mayorLista(lista_numero))

# Imprimir el menor elemento de la lista
print('El menor elemento es: ', menorLista(lista_numero))

# Imprimir la posición del elemento mayor de la lista
print('El elemento mayor se encuentra en la posición: ', posMayList(lista_numero) + 1)

lstResult = posElemMayList(lista_numero)
print('El elemento mayor y su posición es:', lstResult[1], 'Con la posición', lstResult[0] + 1)


# Modificar una lista:
# lista_numero = [10, 15, 20, 30, 40]

lista_numero[-1] = 35

# Operadores de las listas:
lista_numero2 =  [1, 2]

# Operador de concatenación +:
lstrslt = lista_numero + lista_numero2
print(lstrslt)

# Operador (*) de repetición
lstrslt = lista_numero2 * 3
print(lstrslt)
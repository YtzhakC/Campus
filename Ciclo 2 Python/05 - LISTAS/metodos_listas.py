lista = [10, 20, 'Juan', 30, 'Sergio']

lista.append(40) # Añade al final el 40
print(lista)

lista2 = ['Maria', 20]
# append
lista.append(lista2) # Añade los elementos de 'lista2' a lista
#extend
lista.extend(lista2) # Básicamente, hace la misma función que .append()
print(lista)

# insert
lista.insert(2, 50) # Añade '50' en la posición 2 de lista
print(lista)

# pop
lista.pop() # Borra el elemento que le indiques a la función pop
print(lista)

lista.pop(2)
print(lista)

# remove
lista.remove('Sergio')
print(lista)

lista = [40, 30, 5, 90, 20]

# min
print(min(lista)) # Arroja el número menor en la lista

# len
print('Tamaño de la lista:', len(lista)) # Imprime el tamaño de la lista

# sorted
print(sorted(lista)) # Ordena los elementos de la lista de menor a mayor, en forma creciente
# Forma decreciente:
print(sorted(lista, reverse=True)) # reverse=True, significa que hará lo mismo, pero invertido, o sea de forma decreciente, de mayor a menor

lista = [40, 30, 5, 90, 20, 1, 20, 50, 60, 20]

# count
print(lista.count(20)) # Cuenta cuántas veces sale el elemento indicado en la lista

# split
print(lista.split(','))


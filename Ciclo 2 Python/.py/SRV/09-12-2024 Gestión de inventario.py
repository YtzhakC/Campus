inventario = []

def menu():
    print('             ** Gestión de un Inventario **')
    print('1. Agregar un producto')
    print('2. Agregar lote de productos')
    print('3. Eliminar producto del inventario')
    print('4. Eliminar el producto más reciente')
    print('5. Ordenar productos alfabéticamente')
    print('6. Mostrar número total de productos')
    print('7. Salir')

def agregar_producto():
    producto = input("Introduce el nombre del producto: ")
    inventario.append(producto)
    print(f'Producto "{producto}" agregado al inventario.')

def agregar_lote():
    productos = input("Introduce los nombres de los productos, separados por comas: ")
    lista_productos = productos.split(',')
    for producto in lista_productos:
        inventario.append(producto.strip())
    print(f'Lote de productos agregados: {lista_productos}')

def eliminar_producto():
    producto = input("Introduce el nombre del producto que deseas eliminar: ")
    if producto in inventario:
        inventario.remove(producto)
        print(f'Producto "{producto}" eliminado del inventario.')
    else:
        print(f'El producto "{producto}" no está en el inventario.')

def eliminar_reciente():
    if inventario:
        eliminado = inventario.pop()
        print(f'Producto más reciente "{eliminado}" eliminado.')
    else:
        print("El inventario está vacío.")

def ordenar_inventario():
    inventario.sort()
    print("Inventario ordenado alfabéticamente:", inventario)

def mostrar_total():
    print(f'Número total de productos en el inventario: {len(inventario)}')

def gestion_inventario():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            agregar_lote()
        elif opcion == '3':
            eliminar_producto()
        elif opcion == '4':
            eliminar_reciente()
        elif opcion == '5':
            ordenar_inventario()
        elif opcion == '6':
            mostrar_total()
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

gestion_inventario()

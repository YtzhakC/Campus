def clearscreen():
    print(' \n ' * 100)

productos = {}
codigo = 0


def menu():
    print('='*40)
    print('**MENÚ**'.center(40))
    print('-'*40)
    print('Opciones:')
    print('1. Agregar Producto')
    print('2. Buscar Producto')
    print('3. Listar Productos')
    print('4. Listar producto con menos inventario')
    print('5. Listar producto con mayor porcentaje de descuento')
    print('6. Listar producto con menor precio de descuento')
    print('7. Listar producto con mayor precio en inventario')
    print('8. Salir')
    print('>> Escoja una opción (1 - 8)')
    print('-'*40)

def agregar_producto():
        idProducto = {}
        print('\nAñadir Prodcuto:')
        id = input('ID del Producto? \n-> ')
        idProducto[id] = id
        idProducto['name'] = input('Digite el nombre del producto \n-> ')
        idProducto['price'] = float(input('Digite el precio del producto \n-> '))
        idProducto['quantity'] = int(input('Digite la cantidad del producto \n-> '))
        idProducto['discountList'] = int(input('Digite el descuento del producto (Máx 100) \n-> '))
        if idProducto['discountList'] > 100 or idProducto['discountList'] < 0:
            print('El valor del porcentaje de descuento debe ser máximo 100 o debe ser un número entero positivo')
        else:
            productos[id] = idProducto
        

def buscar_producto():
    id = input('Digite la ID del producto que desea buscar')
    if id in productos:
        producto = productos[id]
        print(f"Código: {id}")
        print(f"Nombre: {producto['name'].title()}")
        print(f"Precio: {float(producto['price']):,.2f}")
        print(f"Cantidad: {producto['quantity']:,}")
        print(f"Descuento: {producto['discountList']}% OFF")
        print('')
        print('-' * 40)
    else:
        print(f"Producto con ID {id} no encontrado.")

def listar_productos():
    for id, producto in productos.items():
        print('-'*40)
        print(f"Código: {id}")
        print(f"Nombre: {producto['name'].title()}")
        print(f"Precio: {float(producto['price']):,.2f}")
        print(f"Cantidad: {producto['quantity']:,}")
        print(f"Descuento: {producto['discountList']}% OFF")
        print('')
        print('-' * 40)


def listar_prodcutoMenorI():
    if not productos:  # Verifica si hay productos en el diccionario
        print("No hay productos en el inventario.")
        return
    
    # Inicializar con un valor alto para comparar
    producto_menor_inventario = None
    menor_cantidad = float('inf')
    
    # Recorrer todos los productos
    for id, producto in productos.items():
        cantidad_actual = int(producto['quantity'])  # Convertir a entero para comparar
        if cantidad_actual < menor_cantidad:
            menor_cantidad = cantidad_actual
            producto_menor_inventario = (id, producto)  # Guardamos el producto y su ID
    
    # Si encontramos un producto con menos inventario, lo mostramos
    if producto_menor_inventario:
        id, producto = producto_menor_inventario
        print("Producto con menos inventario:")
        print(f"Código: {id}")
        print(f"Nombre: {producto['name'].title()}")
        print(f"Precio: {float(producto['price']):,.2f}")
        print(f"Cantidad: {producto['quantity']:,}")
        print(f"Descuento: {producto['discountList']}% OFF")
        print('-' * 30)


def listar_productoMayorPD():
    if not productos:  # Verifica si hay productos en el diccionario
        print("No hay productos en el inventario.")
        return
    
    # Inicializar con un valor cero para comparar
    producto_mayor_descuento = None
    mayor_cantidad = 0
    
    # Recorrer todos los productos
    for id, producto in productos.items():
        cantidad_actual = int(producto['discountList'])  # Convertir a entero para comparar
        if cantidad_actual > mayor_cantidad:
            mayor_cantidad = cantidad_actual
            producto_mayor_descuento = (id, producto)  # Guardamos el producto y su ID
    
    # Se muestra el producto con mayor porcentaje de descuento
    if producto_mayor_descuento:
        id, producto = producto_mayor_descuento
        print("Producto con mayor porcentaje de descuento:")
        print(f"Código: {id}")
        print(f"Nombre: {producto['name'].title()}")
        print(f"Precio: {float(producto['price']):,.2f}")
        print(f"Cantidad: {producto['quantity']:,}")
        print(f"Descuento: {producto['discountList']}% OFF")
        print('-' * 30)

def listar_productoMenorPrD():
    if not productos:  # Verifica si hay productos en el diccionario
        print("No hay productos en el inventario.")
        return
    
    # Inicializar con un valor alto (infinito) para comparar
    producto_menor_precio_descuento = None
    menorPrecio = float('inf')
    
    # Recorrer todos los productos
    for id, producto in productos.items():
        cantidad_actual = producto['price'] * (producto['discountList'] / 100)  # Convertir a entero para comparar
        if cantidad_actual < menorPrecio:
            menorPrecio = cantidad_actual
            producto_menor_precio_descuento = (id, producto)  # Guardamos el producto y su ID
    
    # Se muestra el producto con menor precio de descuento
    if producto_menor_precio_descuento:
        id, producto = producto_menor_precio_descuento
        print("Producto con menor precio de descuento:")
        print(f"Código: {id}")
        print(f"Nombre: {producto['name'].title()}")
        print(f"Precio: {float(producto['price']):,.2f}")
        print(f"Cantidad: {producto['quantity']:,}")
        print(f"Descuento: {producto['discountList']}% OFF")
        print('-' * 30)

def listar_productoMayorPI():
    if not productos:  # Verifica si hay productos en el diccionario
        print("No hay productos en el inventario.")
        return
    
    # Inicializar con un valor cero para comparar
    pMayorPrecioInv = None
    mayor_cantidad = 0
    
    # Recorrer todos los productos
    for id, producto in productos.items():
        cantidad_actual = int(producto['price'])  # Convertir a entero para comparar
        if cantidad_actual > mayor_cantidad:
            mayor_cantidad = cantidad_actual
            pMayorPrecioInv = (id, producto)  # Guardamos el producto y su ID
    
    # Se muestra el producto con mayor precio en el inventario
    if pMayorPrecioInv:
        id, producto = pMayorPrecioInv
        print("Producto con mayor precio en el inventario:")
        print(f"Código: {id}")
        print(f"Nombre: {producto['name'].title()}")
        print(f"Precio: {float(producto['price']):,.2f}")
        print(f"Cantidad: {producto['quantity']:,}")
        print(f"Descuento: {producto['discountList']}% OFF")
        print('-' * 30)

def ACME():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            clearscreen()
            agregar_producto()
            clearscreen()
        elif opcion == '2':
            clearscreen()
            buscar_producto()
            clearscreen()
        elif opcion == '3':
            clearscreen()
            listar_productos()
            clearscreen()
        elif opcion == '4':
            clearscreen()
            listar_prodcutoMenorI()
            clearscreen()
        elif opcion == '5':
            clearscreen()
            listar_productoMayorPD()
            clearscreen()
        elif opcion == '6':
            clearscreen()
            listar_productoMenorPrD()
            clearscreen()
        elif opcion == '7':
            clearscreen()
            listar_productoMayorPI()
            clearscreen()
        elif opcion == '8':
            print("Gracias por usar el menú.\nSaliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

ACME()
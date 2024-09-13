
def menu(lst):
    lst = []
    opc = 0
    while opc != 6:

        print(' ')
        print('=' * 50)
        print('                    ** MENÚ **')
        print('1. Agregar libro')
        print('2. Insertar libro en la segunda posición')
        print('3. Eliminar el libro de la tercera posición')
        print('4. Mostrar número total de libros')
        print('5. ordenar e imprimir lista de libros en orden alfabético')
        print('6. Salir')
        print('=' * 50)
        opc = int(input('Digite una opción \n-> '))
        print(' ')
        if opc == 1:
            print('=' * 50)
            book = input('Digite el libro que quiere añadir \n -> ')
            lst.append(book)
            print(f'Listo!, el libro "{book}", se ha añadido correctamente. ')
        elif opc == 2:
            print('=' * 50)
            book = input('Digite el libro que quiera insertar en la posición #2 de la lista: \n -> ')
            lst.insert(2, book)
            print(f'Hecho!, se ha añadido el libro "{book}" a la segunda posición de la lista.')
        elif opc == 3:
            print('=' * 50)
            lst.pop(2)
            print('Listo!, se ha eliminado el libro de la posición #3')
        elif opc == 4:
            print('=' * 50)
            print(f'El número total de libros es:{len(lst)} \n')
        elif opc == 5:
            print('=' * 50)
            print('La lista de libros por orden alfabético es:')
            print(sorted(lst))
        elif opc == 6:
            print('Gracias por usar el software, hasta la próxima!.')
        else:
            print(' ')
            print('>> ERROR. Opción no válida, digite una opción del 1 al 6.')
lista = []
print(menu(lista))

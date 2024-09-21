def menu():
    while True:
        print('** LIBRERIA **')
        print('1. Insertar')
        print('2. Consultar')
        print('3. Salir')

        print('>>> Opcion? ', end='')
        try:
            opcion = int(input())
            if opcion < 1 or opcion > 3:
                print('Error. Opción no válida.')
                print('Presione cualquier tecla para volver al menú...')
                continue
            return opcion
        except ValueError:
            print('Error. Opción no válida.')
            print('Presione cualquier tecla para volver al menú...')
import json
#import pprint

def clear():
    print('\n' * 100)

def guardar(lib):
    with open('Ciclo 2 Python/manejo de errores/libreria.json', 'w') as fd:
        json.dump(lib, fd)

    if not fd.closed: # True si el archivo esta cerrado
        fd.close()


def leerPrecio():
    while True:
        try:
            precio = int(input('Precio del libro?\n-> '))
            if precio < 500:
                print('>>> ERROR. Precio incorrecto.')
                continue
            return precio
        except ValueError:
            print('>>> ERROR. Precio inválido.')

def leerAutor():
    while True:
        try:
            autor = input('Autor del libro?\n-> ')
            if len(autor.strip()) == 0:
                print('>>> ERROR. Autor inválido.')
                continue
            return autor
        except Exception as e:
            print('Error al ingresar el autor.\n' + e)

def leerTitulo():
    while True:
        try:
            tit = input('Título del libro?\n-> ')
            if len(tit.strip()) == 0:
                print('>>> ERROR. Título inválido.')
                continue
            return tit
        except Exception as e:
            print('Error al ingresar el título.\n' + e)

def leerCodigo():
    while True:
        try:
            cod = input('Código del libro?\n-> ')
            if len(cod.strip()) == 0:
                print('>>> ERROR. Código inválido.')
                continue
            return cod
        except Exception as e:
            print('Error al ingresar el código.\n' + e)

def insertar(lib):
    print('\n\n** 1. INSERTAR **')
    cod = leerCodigo()
    if cod not in lib:

        titulo = leerTitulo()
        autor = leerAutor()
        precio = leerPrecio()

        datLib = {
            'titulo' : titulo,
            'autor': autor,
            'precio': precio
        }

        lib[cod] = datLib

        #pprint.pprint(lib)
        lib = dict(sorted(lib.items()))
        #pprint.pprint(lib)
    else:
        print('El codigo ya existe en la libreria.')

    input('Presione cualquier tecla para volver al menú...')

    return lib

def consultar(lib):
    print('\n\n** 2. CONSULTAR **')
    input('Presione cualquier tecla para volver al menú...')

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


# PROGRAMA PRINCIPAL

libreria = {}

while True:
    op = menu()
    match op:
        case 1:
            clear()
            libreria = insertar(libreria)
            guardar(libreria)
            clear()
        case 2:
            clear()
            consultar(libreria)
            clear()
        case 3:
            clear()
            print('\nGracias por usar el software.\n')
            break
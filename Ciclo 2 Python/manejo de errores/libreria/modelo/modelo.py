# import pprint

from persistencia.persistencia import guardar

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

        guardar(lib)
    else:
        print('El codigo ya existe en la libreria.')

    input('Presione cualquier tecla para volver al menú...')

    return lib

def consultar(lib):
    print('\n\n** 2. CONSULTAR **')

    cod = input('\nCódigo del libro? ')

    if cod in lib:
        print('-> Codigo', cod)
        print(f'Título: {lib[cod]["titulo"]}')
        print(f'Autor: {lib[cod]["autor"]}')
        print(f'Precio: ${lib[cod]["precio"]}')
    else:
        print('>>> Error. El código del libro no existe en la librería.')

    input('Presione cualquier tecla para volver al menú...')
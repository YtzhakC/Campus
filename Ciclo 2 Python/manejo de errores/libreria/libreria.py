from Interfaz.menu import menu
from modelo.modelo import insertar, consultar
from persistencia.persistencia import cargar


def clear():
    print('\n' * 100)

# PROGRAMA PRINCIPAL

libreria = {}
archivo = 'Ciclo 2 Python/manejo de errores/libreria/libreria.json'
libreria = cargar(archivo)

# print(libreria)

while True:
    op = menu()
    match op:
        case 1:
            clear()
            libreria = insertar(libreria, archivo)
            clear()
        case 2:
            clear()
            consultar(libreria)
            clear()
        case 3:
            clear()
            print('\nGracias por usar el software.\n')
            break

def menu(lst):
    lst = []
    opc = 0
    while opc != 6:

        print(' ')
        print('=' * 50)
        print('              ** ASISTENCIA **')
        print('1. Registrar Estudiante')
        print('2. Corregir nombre del estudiante')
        print('3. Ver último estudiante en registrarse')
        print('4. Mostrar lista completa de asistencia')
        print('5. Mostrar número total de asistentes')
        print('6. Salir')
        print('=' * 50)
    
        opc = int(input('Digite una opción \n-> '))
        print(' ')

        if opc == 1:
            print('=' * 50)
            student = input('Digite el nombre del estudiante que desee añadir \n -> ')
            lst.append(student)
            print(f'Listo!, el estudiante "{student}", se ha añadido correctamente. ')
        elif opc == 2:
            print('=' * 50)
            n = int(input('Digite el número de estudiante que desee corregir: \n -> '))
            student = input('Digite el nombre del estudiante: \n-> ')
            lst[n-1] = student
            print('Hecho!, se ha corregido el estudiante correctamente.')
        elif opc == 3:
            print('=' * 50)
            print(f'El último estudiante en registrarse es: {lst[-1]}')
            print('=' * 50)
        elif opc == 4:
            print('=' * 50)
            print('La asistencia es: ')
            for i in range(len(lst)):
                print(f'{i+1}. {lst[i]}')
            print('=' * 50)
        elif opc == 5:
            print('=' * 50)
            print(f'El número total de asistentes es: {len(lst)}')
            print('=' * 50)
        elif opc == 6:
            print('-' * 50)
            print('Gracias por usar el software, hasta la próxima!.')
            print('-' * 50)
        else:
            print(' ')
            print('>> ERROR. Opción no válida, digite una opción del 1 al 6.')
lista = []
print(menu(lista))

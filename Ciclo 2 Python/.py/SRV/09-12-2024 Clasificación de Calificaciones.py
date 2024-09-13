
def menu(lst):
    lst = []
    opc = 0
    while opc != 7:

        print(' ')
        print('=' * 50)
        print('           ** CALIFICACIÓNES **')
        print('1. Ver calificación más alta')
        print('2. Ver calificación más baja')
        print('3. Ordenar calificaciones de menor a mayor')
        print('4. Eliminar calificación incorrecta')
        print('5. Mostrar promedio de calificaciones')
        print('6. Mostrar número total de estudiantes')
        print('7. Salir')
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
        elif opc == 7:
            print('-' * 50)
            print('Gracias por usar el software, hasta la próxima!.')
            print('-' * 50)
        else:
            print(' ')
            print('>> ERROR. Opción no válida, digite una opción del 1 al 7.')
lista = []
print(menu(lista))

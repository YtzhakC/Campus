def imprimirLista(lst):
    for e in lst:
        print(e, end=' | ')
        print('')

n = int(input('Cuántas letras va a ingresar? \n-> '))
lstvocales = [0] * 5 # Es lo mismo que: lstvocales = [0, 0, 0, 0, 0]

for i in range(n):
    letra = input(f'Ingrese la letra {i+1} \n-> ')

    letra = letra.strip()
    if len(letra) > 0:
        letra = letra[0].lower()
        # if letra.lower() == 'a':
        #     lstvocales[0] += 1
        # elif letra.lower() == 'e':
        #     lstvocales[1] =+ 1
        # elif letra.lower() == 'i':
        #     lstvocales[2] =+ 1
        # elif letra.lower() == 'o':
        #     lstvocales[3] =+ 1
        # elif letra.lower() == 'u':
        #     lstvocales[4] =+ 1

        match letra:
            case 'a':
                lstvocales[0] += 1
            case 'e':
                lstvocales[1] += 1
            case 'i':
                lstvocales[2] += 1
            case 'o':
                lstvocales[3] += 1
            case 'u':
                lstvocales[4] += 1
            case _:
                pass
                

print('=' * 40)
print('')
imprimirLista(lstvocales)


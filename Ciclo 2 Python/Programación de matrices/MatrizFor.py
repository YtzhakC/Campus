import random

"""
mat(2, 3)

# Column  0      1     2
mat = [ [None, None, None], # fila 0
        [None, None, None]  # fila 1
       ]
"""

def crearMat(fil, col):
    matriz = []
    for f in range(fil):
        matriz.append([None]* col)
    return matriz

def printMat(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print(mat[f][c], end='\t')
        print('') # Cambia de linea después del último tabulador (\t)

def inputMatriz(mat):
    for f in range(len(mat)):
        print(f'Fila {f+1}')
        for c in range(len(mat[f])):
            mat[f][c] = int(input(f'mat[{f}][{c}]? '))

        print('-' * 10, '\n')

def randomMatriz(mat, ini, fin):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat[f][c] = random.randrange(ini, fin)

def matrizIdentidad(mat):
    tamf = len(mat)
    tamc = len(mat[0])
    if tamf == tamc: 
        for f in range(tamf):
            for c in range(tamc):
                if f != c:
                    mat[f][c] = 0
                else:
                    mat[f][c] = 1
        return mat
    else:
        return None 
# Matrices
def ingresarDatosMat(mat):
    for f in range(len(mat)):
        print(f'Ingrese datos de la fila {f}')
        for c in range(len(mat[f])):
            mat[f][c] = int(input(f'mat[{f+1}][{c+1}]? '))

def imprimirMat(m):
    for f in range(len(m)):
        for c in range(len(m[f])):
            print(m[f][c], end='\t')
        print('')

def crearMatriz(fil, col):
    m = []
    for f in range(fil):
        m.append([None] * col)
    return m

m = [[1, 2, 3], # Fila 0
     [4, 5, 6]] # Fila 1
# Matriz 2x3

# Imrpimir la fila completa
print(m[0])

# Imprimir el 5
print(m[1][1])

mat = []
mat = crearMatriz(3, 5)

# imprimirMat(mat)
# mat[2][2] = 15
# print('='*50)
# imprimirMat(mat)

ingresarDatosMat(mat)
imprimirMat(mat)
# Algoritmo que duplique los n datos ingresados
 
def duplicar(lst):
    lrta = []
    for e in lst:
        lrta.append(e*2)
    return lrta
    
n = int(input('Ingrese la cantidad de datos: -> '))
lstNum = []
for i in range(n):
    lstNum.append(int(input(f'Ingrese el dato #{i+1}: ')))

print(duplicar(lstNum))

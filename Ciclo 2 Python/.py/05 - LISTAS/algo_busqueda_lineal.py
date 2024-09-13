from networkx import NetworkXAlgorithmError


def  busquedaLineal(lst, elem): # Se pide la lista y el elemento a buscar
    for i in range(len(lst)):
        if lst[i] == elem:
            return [True, i]
    return [False, None]

lista = ['Carlos', 'Daniel', 'Maria', 'Laia', 'Angel', 'Oscar', 'Coquetin']

existe, pos = busquedaLineal(lista, 'Coquetin')
if existe: # existe == True
    print('Pasa al ciclo 3')
    print(f'Posición: {pos} ')
else:
    print('Muchas Gracias por estar en Campus')
  # Lista = []
  # Tuplas = ()
  # Conjuntos = {}

#            ERES MI AMIGO NEGRO 
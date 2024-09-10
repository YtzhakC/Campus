# Función que reciba un número y devuelva "True" si es primo, o "False" si no lo es

def esprimo(num):
    if num > 1:
        es_primo = True
        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break

        if es_primo: # Es equivalente a: esprimo == True
            return True
        else:
            return False

    else:
        return False
    

    # Programa que reciba una serie de números hasta que se ingrese un primo
n = int(input('Digite un número: \n'))
while not esprimo(n):
    n = int(input('Digite un número: \n'))
    
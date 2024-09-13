def is_palindrome(s):
    reverse = s[::-1]
    if (s == reverse):
        return True
    return False

n = int(input('Ingrese la cantidad de palabras:'))
lista = []
lista2 = []
for i in range(n):
    palabra = input('Digite la palabra: \n ->').lower()
    lista.append(palabra)
    if is_palindrome(palabra):
        lista2.append('True')
    else:
        lista2.append('False')


print(','.join(lista2).lower())
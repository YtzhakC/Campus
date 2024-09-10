# RECORRIDO DE CADENAS

# 1. Por sus elementos (Carácteres)
s = 'Voy volando...'
for c in s:
    print(c, end='')

# Ejemplo: ¿Cuántas vocales hay en la cadena?
vocales = 0
for c in s:
    if c == 'a' or c == 'A' \
    or c == 'e' or c == 'E' \
    or c == 'i' or c == 'I' \
    or c == 'o' or c == 'O' \
    or c == 'u' or c == 'U':
        vocales +=1

print(f'\nCantidad de vocales: {vocales}\n')

# 2. Por su ÍNDICE
print('=' * 40)
for i in range(len(s)):
    print(s[i], end='')

# Ejemplo: Cuántas vocales hay en la cadena
vocales = 0
for i in s:
    if s[i] == 'a' or s[i] == 'A' \
    or s[i] == 'e' or s[i] == 'E' \
    or s[i] == 'i' or s[i] == 'I' \
    or s[i] == 'o' or s[i] == 'O' \
    or s[i] == 'u' or s[i] == 'U':
        vocales +=1

# Ejemplo: En qué posición de la cadena está el primer espacio?
for i in range(len(s)):
    if s[i] == ' ':
        break
print(f'El primer espacio está en la posición: {i}.')

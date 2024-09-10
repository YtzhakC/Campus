# Crear una función que valide si una contraseña es aceptable
# Es aceptable cuando:
# Tenga de 3 a 20 carácteres

def validPassword(contra):
    longContra = len(contra)
    if longContra >= 3 and longContra <= 20:
        return True
    else:
        return False
    
# Programa que valide una contraseña
passw = input('Digite la contraseña: \n')
while not validPassword(passw): # validPassword(passw) == False
    passw = input('Digite la contraseña: \n')

print('\nAcceso Permitido.')

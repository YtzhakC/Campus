# DICCIONARIOS

dCampers = {1:'Ada', 2:'Juan', 3:'Diego', 4:'Oscar', 5:'Anderson'}
print(dCampers)

# Crear un diccionario vacío
# dCampers = {} 
# dCampers = dict()
# print(dCampers)

# SETDEFAULT()
print(dCampers.setdefault(4)) # Esto cuando existe la llave.

print(dCampers.setdefault(6, 'Maria')) # Esto cuando la llave no existe. se puede crear la llave y su respectivo valor añadiendolo con coma, así como en el diccionario principal
print(dCampers)

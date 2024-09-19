persona = {'nombre':'Juan', 'edad':30, 'apellido':'López'}
# Lo que hay antes de los dos puntos es la clave, y lo que hay despues de los dos puntos es el contenido

print(persona['nombre'])

print(len(persona))
# in - Busca la llave que le pidas dentro del diccionario, si pongo 'Juan' in persona, me devolverá false,
# porque 'Juan' es el contenido, y 'nombre' es la llave.
print('nombre' in persona)
print('Juan' in persona)


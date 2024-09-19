import json

# lista = ['Daniel', 'Maria', 'Ada', 'Julian', 'Gabriel', ['Julian', 'Ricardo']]
# Se crea un diccionario de campers:
campers = {
    1: {
        'nombre': 'Daniel',
        'edad': 21,
        'sexo': 'm',
        'telefonos': [123, 456]
    },
    2: {
        'nombre': 'Maria',
        'edad': 20,
        'sexo': 'f',
        'telefonos': [789]
    }
}

with open("Ciclo 2 Python/.py/ARCHIVOS JSON/datos.json", 'w') as fd:
    json.dump(campers, fd)

if not fd.closed: # True si el archivo esta cerrado
    fd.close()
import json
import pprint

with open("Ciclo 2 Python/.py/ARCHIVOS JSON/datos.json", "r") as fd:
    estructura = json.load(fd)

pprint.pprint(estructura)
print(type(estructura))
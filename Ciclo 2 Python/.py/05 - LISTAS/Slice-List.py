lst = [10, 20, 30, 40, 50]

print(lst[:-1])
print(lst[1:-1])
print(lst[::2])
print(lst[::-1])
print(lst[::-2])


# Diccionarios

capitales = {'Colombia':'Bogotá', 'Perú':'Lima', 'Argentina':'BuenosAires'}

empleado = {'nombre':'Sergio', 'apellido':'Medina','cargo':'Programador','salario':4000000}

empleado['nombre'] # Acá con llaves
# Es lo mismo que:
empleado.get('nombre') # Acá con paréntesis

# empleado['email'] Tira error porque no existe.
empleado.get('email', 'NO ENCONTRADO')
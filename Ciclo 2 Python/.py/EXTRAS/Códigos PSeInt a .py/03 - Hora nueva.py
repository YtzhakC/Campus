hora = int(input("Digite la hora: \n"))
min = int(input("Digite los minutos: \n"))
min_add = int(input("Digite los minutos a añadir: \n"))

new_min = min + min_add

new_hora = hora + (new_min//60)
new_min = new_min % 60
if new_hora >= 24:
    new_hora = new_hora - 24

print(f"Nueva hora: {new_hora}:{new_min}")
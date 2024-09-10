nick = input("Digite el nombre del conductor: ")

placa = input("Digite la placa del vehículo: ")

valor_pasajes = int(input("Digite el total obtenido en pasajes: "))

valor_encomienda = int(input("Digite el valor total en encomiendas: "))

pago = (valor_pasajes*0.25) + (valor_encomienda*0.15)


print("---------------------------------------------------")
print("Nombre: ", nick)
print("---------------------------------------------------")
print("Placa del vehículo: ", placa)
print("---------------------------------------------------")
print(f"Valor total de pasajes: {valor_pasajes:,.2f}")
print("---------------------------------------------------")
print(f"Valor total de encomiendas: {valor_encomienda:.2f}")
print("---------------------------------------------------")
print(f"Valor a pagar por pasajes: {(valor_pasajes*0.25):,.2f}")
print("---------------------------------------------------")
print(f"Valor a pagar por encomiendas: {(valor_encomienda*0.15):,.2f}")
print("---------------------------------------------------")
print(f"El valor de liquidación del conductor es de: {pago:,.2f} ")
print("---------------------------------------------------")
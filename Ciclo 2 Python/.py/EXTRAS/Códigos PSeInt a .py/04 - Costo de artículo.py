desc_art = input("Ingrese el artículo: \n")
cant = int(input("Ingrese la cantidad de artículos a llevar: \n"))
price = int(input("Digite el precio unitario del artículo: \n"))

f_price = price*cant
IVA = f_price * 0.20
cash_acc = f_price + IVA
print(" ")
print("-----------------------------------------------------------")
print(f"Descripción Atrículo: {desc_art}")
print(f"Cantidad pedida: {cant}")
print(f"Precio: {f_price:,.0f}")
print(f"IVA (20%): {IVA:,.0f}")
print(f"Valor final: {cash_acc:,.0f}")
print("-----------------------------------------------------------")

price = int(input("Ingrese el precio del producto: \n"))

if price >= 100:
    discount = price*0.10
    new_price = price - discount
    print(f"El precio con un 10% de descuento es de: {new_price}")
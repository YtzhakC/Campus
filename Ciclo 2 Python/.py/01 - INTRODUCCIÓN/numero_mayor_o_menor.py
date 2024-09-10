n1 = int(input("Digite el primer número: \n"))
n2 = int(input("Digite el segundo número: \n"))
n3 = int(input("Digite el tercer número: \n"))

if (n1 >= n2) and (n1 >= n3):
    if n2 >= n3:
        print("Los números de mayor a menor son: ")
        print(n1)
        print(n2)
        print(n3)
    else:
        print("Los números de mayor a menor son: ")
        print(n1)
        print(n3)
        print(n2)
elif (n2 >= n1) and (n2 >= n3):
    if n1 >= n3:
        print("Los números de mayor a menor son: ")
        print(n2)
        print(n1)
        print(n3)
    else:
        print("Los números de mayor a menor son: ")
        print(n2)
        print(n3)
        print(n1)
elif (n3 >= n1) and (n3 >= n2):
    if n1 >= n2:
        print("Los números de mayor a menor son: ")
        print(n3)
        print(n1)
        print(n2)
    else:
        print("Los números de mayor a menor son: ")
        print(n3)
        print(n2)
        print(n1)

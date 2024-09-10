nick = input("Digite su nombre: ")
nr1 = float(input("Digite la nota del reto 1: "))
nr2 = float(input("Digite la nota del reto 2: "))
nr3 = float(input("Digite la nota del reto 3: "))
ni = float(input("Digite la nota de inglés: "))

total = (nr1*0.20) + (nr2*0.25) + (nr3*0.35) + (ni*0.20)
print(nick,", Tu nota definitiva es: {:.1f}". format(total))
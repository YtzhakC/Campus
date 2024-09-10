hijo = ""
sw = True
while sw == True:
    print(" ")
    mama_traumada = str(input("La mamá tiene ego y está traumada? (Sí o No) \n"))
    if (mama_traumada == "SI" or mama_traumada == "Si" or mama_traumada == "si"):
        sw = True
        print(" ")
        hijo = "El niño tendrá traumas y va a pegar niñas en el colegio."
        print(hijo)
        print(" ")
    elif (mama_traumada == "NO" or mama_traumada == "No" or mama_traumada == "no"):
        sw = False
        print(" ")
        hijo = "El niño no tendrá trauma y no va a pegar niñas en el colegio."
        print(hijo)
        print(" ")
    else:
        sw = True
        print(" ")
        print(">> ERROR. No válido... Por favor, escriba Sí o No")
        print(" ")

birth = int(input('Digite su dia de nacimiento: \n'))

if (birth >= 1 and birth <= 15):
    print('Naciste en la primera quincena.')
elif (birth >= 16 and birth <= 30):
    print('Naciste en la segunda quincena.')
else:
    print('Naciste a final de mes.')
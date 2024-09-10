age = int(input('Digite su edad: \n'))

if (age >= 0 and age <= 12):
    print('Eres un Niño.')
elif (age >= 13 and age <= 17):
    print('Eres un Adolescente.')
elif (age >= 18 and age <= 35):
    print('eres un Adulto Joven.')
elif (age >= 36 and age <= 65):
    print('Eres un Adulto.')
else:
    print('Eres mayor.')
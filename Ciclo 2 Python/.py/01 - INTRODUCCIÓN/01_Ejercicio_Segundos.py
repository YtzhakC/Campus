
print("Conversor de segundos a minutos y horas")
segundos = float(input("Introduzca segundos: "))
minutos = segundos / 60
horas = minutos / 60
minutosFinal = minutos % 60
segundosFinal = segundos % 60
print(f"las horas minutos son: {horas:.0f} horas, {minutosFinal:.0f} minutos, {segundosFinal:.0f} segundos")
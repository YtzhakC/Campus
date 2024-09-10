hour = int(input('Digite la hora: \n'))
min = int(input('Digite los minutos \n'))
if hour > 24:
    hour = hour-24
if min > 59:
    min = min%60

if (hour >= 5 and hour <= 11):
    print(f'Son las {hour}:{min}. Buenos días')
elif (hour >= 12 and hour <= 17):
    print(f'Son las {hour}:{min}. Buenas tardes')
else:
    print(f'Son las {hour}:{min}. Es hora de dormir.')
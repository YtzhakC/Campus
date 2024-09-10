i_tuition = 10_000
f_tuition = 20_000
count = 0

while i_tuition < f_tuition:
    i_tuition += (i_tuition*0.07)
    count += 1

print(f'In {count} years, tuition cost is: {i_tuition:,.2f} $')
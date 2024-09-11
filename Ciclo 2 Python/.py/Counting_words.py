
n = int(input('How many words will you type? \n-> '))
pref = input('What prefix will you search? \n-> ')
cpre = 0
for i in range(1, n+1):
    s = input(f'Type the {i} word: \n->')

    if s.startswith(pref) == True:
        cpre +=1

print(cpre)
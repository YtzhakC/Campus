def same_first_last(lst): 
    if len(lst) >= 2:
        # if lst[0] == lst[-1]:
        #     return True
        return lst[0] == lst[-1]

n = int(input('Enter how many words you will put in the list: \n-> '))
lista = []
for i in range(n):
    word = input(f'Enter the word #{i+1}: \n-> ')
    lista.append(word)
if same_first_last(lista):
    print(same_first_last(lista))

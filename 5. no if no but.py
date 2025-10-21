#made this without starting learning the if chapter XD

a=3
if (a==2):
    print("hello")
elif(a!=2):
    print("bye")

#mixing lists with if statements

names=['eenie','minnie','penguiny','mo']
for na in names:
    print(na)

    if(na=="eenie"):
        print(f'hi this is {na}, find me minnie')
    elif(na=="minnie"):
        print(f'hi this is {na}, find me penguiny')
    elif(na=="penguiny"):
        print(f'hi this is {na}, find me mo')
    else:
        print(f'this is {na}, give me any')

#alien attack

alien=['thor','hulk','loki','cap america']
for al in alien:
    if al=='thor':
        print(f"did you just killed {al}, you earned 5 points for that")
    elif al=='hulk':
        print(f"did you just killed {al}, you earned 10 points for that")
    elif al=='loki':
        print(f"did you just killed {al}, you earned 100 points for that")
    else:
        print(f"bro did you just killed {al}, you earned 500 points for that")

#alien attack 2

alien='loki'

if alien=='thor':
        print(f"did you just killed thor, you earned 5 points for that")
elif alien=='hulk':
        print(f"did you just killed hulk, you earned 10 points for that")
elif alien=='loki':
        print(f"did you just killed loki, you earned 100 points for that")
else:
        print(f"bro did you just killed cap, you earned 500 points for that")


#if else list project to get best pizza

shop=['macaroni','cheese','pepper','bell pepper','capsicum','pineapple']
b=input("tell me the topping you want: ")
if b=='macaroni':
        print(f"great choice, adding {b}, your total would be 50$")
elif b=='cheese':
        print(f"great choice, adding {b}, your total would be 20$")
elif b=='pepper':
        print(f"great choice, adding {b}, your total would be 10$")
elif b=='bell pepper':
        print(f"great choice, adding {b}, your total would be 15$")
elif b=='capsicum':
        print(f"great choice, adding {b}, your total would be 25$")
elif b=='pineapple':
        print(f"great choice, adding {b}, your total would be 5$")
elif b=='':
        print("you sure you want plain pizza?")
else:
        print(f"sorry we don't have {b} currently ")